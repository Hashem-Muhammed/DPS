from django.db import models
from django.core.validators import FileExtensionValidator


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    width = models.IntegerField()
    height = models.IntegerField()
    number_of_channels = models.IntegerField()

    def __str__(self):
        return f"{self.id}"


class Document(models.Model):
    document = models.FileField(upload_to="documents/")
    number_of_pages = models.IntegerField()
    page_width = models.IntegerField()
    page_height = models.IntegerField()

    def __str__(self):
        return f"{self.id}"
