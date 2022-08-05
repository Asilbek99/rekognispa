from django.db import models
from pages.models import Image


class FaceDetection(models.Model):
    image_fr = models.ForeignKey(Image, on_delete=models.CASCADE)
    orignal_image_url = models.URLField(max_length=256)
    rekognized_image_url = models.URLField(max_length=256)
    gender = models.CharField(max_length=16)
    age_low = models.IntegerField(blank=True, null=True)
    age_high = models.IntegerField(blank=True, null=True)
    emotion = models.CharField(max_length=64)
    # feature = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}: {self.image_fr}"


class Features(models.Model):
    face_fr = models.ForeignKey(FaceDetection, on_delete=models.CASCADE)
    beard = models.BooleanField(blank=True, null=True)
    smile = models.BooleanField(blank=True, null=True)
    eyeglasses = models.BooleanField(blank=True, null=True)
    sunglasses = models.BooleanField(blank=True, null=True)
    mustache = models.BooleanField(blank=True, null=True)
    eyes_open = models.BooleanField(blank=True, null=True)
    mouth_open = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}: {self.face_fr}"


class BoundingBox(models.Model):
    fr_feature = models.ForeignKey(Features, on_delete=models.CASCADE)
    height = models.IntegerField()
    width = models.IntegerField()
    left = models.IntegerField()
    top = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.fr_feature}"
