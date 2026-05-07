from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=500)
    file_path = models.FileField(upload_to='videos/', blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='processing')

    def __str__(self):
        return self.title

class Summary(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    summary_text = models.TextField(blank=True)
    key_points = models.TextField(blank=True)
    transcript = models.TextField(blank=True)
    language = models.CharField(max_length=50, default='English')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Summary of {self.video.title}"