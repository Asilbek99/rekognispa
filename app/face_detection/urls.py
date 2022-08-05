from django.urls import path
from .views import FaceDetectionDetailView, FaceDetectionListView

urlpatterns = [
    path('', FaceDetectionListView.as_view(), name='face_list'),
    path('<pk>/', FaceDetectionDetailView.as_view(), name='face_detail'),
]
