import boto3
import io
from PIL import Image, ImageDraw, ImageFont
import os


def show_faces(photo, bucket):

    client = boto3.client('rekognition')
    # Load image from S3 bucket
    s3_connection = boto3.resource('s3')
    s3_object = s3_connection.Object(bucket, photo)
    s3_response = s3_object.get()

    stream = io.BytesIO(s3_response['Body'].read())
    image = Image.open(stream)

    # Call DetectFaces
    response = client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
                                   Attributes=['ALL'])

    imgWidth, imgHeight = image.size
    draw = ImageDraw.Draw(image)
    # image.setfont("HelveticaNarrow-Bold", 36)

    image_title = photo[photo.rfind('/')+1:photo.find('.')]
    image_format = image.format

    # calculate and display bounding boxes for each detected face
    for faceDetail in response['FaceDetails']:

        box = faceDetail['BoundingBox']
        left = imgWidth * box['Left']
        top = imgHeight * box['Top']
        width = imgWidth * box['Width']
        height = imgHeight * box['Height']
        image_label = f"Gender: {faceDetail['Gender']['Value']}, Emotion: {faceDetail['Emotions'][0]['Type']}, Age: {faceDetail['AgeRange']['Low']}"


        points = (
            (left, top),
            (left + width, top),
            (left + width, top + height),
            (left, top + height),
            (left, top)
        )
        draw.line(points, fill='#00d400', width=2)
        draw.text((left, top - 20), image_label, fill="cyan", anchor="ms")
        for landmark in faceDetail['Landmarks']:
            x = landmark['X']
            y = landmark['Y']
            draw.ellipse((imgWidth*x, imgHeight*y, imgWidth*x+3, imgHeight*y+3), fill='red')

    in_mem_file = io.BytesIO()
    image.save(in_mem_file, format=image_format)
    in_mem_file.seek(0)

    return {"face_details": response['FaceDetails'], "image": {"stream": in_mem_file, "title": image_title,"format": image_format }}
    