from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)  # Add this line to track views

    def increment_views(self):
        self.views += 1
        self.save()

    def __str__(self):
        return self.title
