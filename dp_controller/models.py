from django.db import models
from django.core.validators import FileExtensionValidator
import PIL.Image
import os
from django.core.files import File
from DPS import settings
from pdf2image import convert_from_path


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    width = models.IntegerField()
    height = models.IntegerField()
    number_of_channels = models.IntegerField()

    def __str__(self):
        return f"{self.id}"

    def rotate_image_by(self, angle):
        original_image = PIL.Image.open(self.image)
        rotated_image = original_image.rotate(angle)
        rotated_image_path = f"../mediafiles/{self.image.name}"
        rotated_image.save(os.path.join(settings.MEDIA_ROOT, rotated_image_path))
        self.image = File(open(rotated_image_path, "rb"), name=self.image.name)


class Document(models.Model):
    document = models.FileField(upload_to="documents/")
    number_of_pages = models.IntegerField()
    page_width = models.IntegerField()
    page_height = models.IntegerField()

    def __str__(self):
        return f"{self.id}"

    def convert_to_image(self):
        path = self.document.path
        images = convert_from_path(
            path,
            poppler_path=r"C:\Users\Lenovo\Downloads\Release-21.11.0-0\poppler-21.11.0\Library\bin",
        )
        for i, image in enumerate(images):
            new_name = f"{self.document.name[:-3]}jpg"
            image.save(f"../mediafiles/{new_name}", "JPEG")
            image_path = f"../mediafiles/{new_name}"

            image_instance = Image(
                image=File(open(image_path, "rb"), name=new_name),
                width=image.width,
                height=image.height,
                number_of_channels=0,
            )
            image_instance.save()
            return image_instance
