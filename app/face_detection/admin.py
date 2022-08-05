from django.contrib import admin

# Register your models here.
from .models import FaceDetection, Features

admin.site.register([FaceDetection, Features])
