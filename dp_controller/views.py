from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ImageSerializer, DocumentSerializer
from rest_framework.response import Response
from rest_framework import status
from .services import b64_to_pdf
from rest_framework import viewsets
from .models import *
# Create your views here.
@api_view(["POST"])
def upload_file(request):
    if request.data.get("image"):
        serializer = ImageSerializer(data=request.data)
    elif request.data.get("document"):
        request.data._mutable = True
        request.data["document"] = b64_to_pdf(request.data["document"])
        request.data._mutable = False

        serializer = DocumentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

