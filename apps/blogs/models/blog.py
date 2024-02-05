from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    content = models.TextField()

    views = models.IntegerField(default=0)
    post_banner = models.ImageField(upload_to='post_banners/')
    read_time = models.IntegerField()
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"