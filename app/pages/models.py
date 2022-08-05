from django.db import models
from django.db.models.signals import post_save
from face_detection.services import show_faces
from accounts.models import UserProfile
import face_detection.models as face_detection_models
import os
import boto3

s3 = boto3.client('s3')


class Image(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    RECOGNITION_TYPES = (
        ('FACE', 'Face Rekognition'),
    )

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/root')
    rekognition_type = models.CharField(
        max_length=6,
        choices=RECOGNITION_TYPES,
        default=None
    )

    def __str__(self):
        return f"{self.id}: {self.title} in {self.rekognition_type}"


# performing recognition after saving image
def save_image(sender, instance, created, **kwargs):
    photo, bucket, bucket_url = instance.image.name, os.environ.get(
        'S3_BUCKET_NAME'), os.environ.get('S3_BUCKET_URL')
    if instance.rekognition_type == 'FACE':
        # for face detection
        rekog_data = show_faces(photo, bucket)

        rekognized_image = rekog_data['image']['stream']
        rekognized_image_title = rekog_data['image']['title']
        rekognized_image_format = rekog_data['image']['format']
        rekognized_image_s3_path = 'images/faces/' + rekognized_image_title + '.' + rekognized_image_format

        # uploading rekognize image to s3 using boto3
        s3.upload_fileobj(
            rekognized_image,
            bucket,
            rekognized_image_s3_path,
        )

        for rekog_data in rekog_data['face_details']:

            orignal_image_url = bucket_url + photo
            rekognized_image_url = bucket_url + rekognized_image_s3_path
            gender = rekog_data['Gender']['Value']
            age_low = rekog_data['AgeRange']['Low']
            age_high = rekog_data['AgeRange']['High']
            emotion = rekog_data['Emotions'][0]['Type']

            # updating face recognition details in database after get data from AWS rekognition API
            face_detection = face_detection_models.FaceDetection(
                image_fr=instance,
                rekognized_image_url=rekognized_image_url,
                orignal_image_url=orignal_image_url,
                gender=gender,
                age_low=age_low,
                age_high=age_high,
                emotion=emotion
            )

            beard = rekog_data['Beard']['Value']
            smile = rekog_data['Smile']['Value']
            eyeglasses = rekog_data['Eyeglasses']['Value']
            sunglasses = rekog_data['Sunglasses']['Value']
            mustache = rekog_data['Mustache']['Value']
            eyes_open = rekog_data['EyesOpen']['Value']
            mouth_open = rekog_data['MouthOpen']['Value']

            face_detection.save()

            # updating face features in database after get data from AWS rekognition API
            features = face_detection_models.Features(
                face_fr=face_detection,
                beard=beard,
                smile=smile,
                eyeglasses=eyeglasses,
                sunglasses=sunglasses,
                mustache=mustache,
                eyes_open=eyes_open,
                mouth_open=mouth_open
            )

            features.save()


post_save.connect(save_image, sender=Image)
