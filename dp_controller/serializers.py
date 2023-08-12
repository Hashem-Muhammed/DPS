from rest_framework import serializers
from .models import Image, Document
from drf_extra_fields.fields import Base64ImageField, Base64FileField
from django.core.files.base import ContentFile
from base64 import b64decode


class ImageSerializer(serializers.ModelSerializer):
    image=Base64ImageField()
    class Meta:
        model = Image
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Document
        fields = "__all__"

