from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_video, name='upload'),
    path('summarize/', views.summarize_video, name='summarize'),
    path('videos/', views.get_videos, name='videos'),
]