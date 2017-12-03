from django.db import models

# Create your models here.


class Presentation(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=2048, null=True, blank=True)
    image = models.ImageField(upload_to='presentations', null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Presentation | { self.title }>"

    def __str__(self):
        return self.title
