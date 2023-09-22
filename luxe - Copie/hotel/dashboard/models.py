from django.db import models

class DashboardItem(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    images = models.ImageField(null=True, blank=True, upload_to='dashboard_images/', max_length=255)

    def __str__(self):
        return self.title

