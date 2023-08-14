from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ImageSerializer, DocumentSerializer
from rest_framework.response import Response
from rest_framework import status
from .services import b64_to_pdf
from rest_framework import viewsets
from .models import *
from django.shortcuts import get_object_or_404



@api_view(["POST"])
def upload_file(request):
    if request.data.get("image"):
        serializer = ImageSerializer(data=request.data)
    elif request.data.get("document"):
        request.data["document"] = b64_to_pdf(request.data["document"])
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

@api_view(['POST'])
def rotate_image(request):
    image_id = request.data.get('id', None)
    rotate_angel = request.data.get('rotate_angel', None)
    if image_id and rotate_angel:
        image = get_object_or_404(Image , id = image_id)
        image.rotate_image_by(int(rotate_angel))
        image.save()
        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response( status = status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def pdf2images(request):
    pdf_id = request.data.get('id',None)
    if pdf_id:
        pdf = get_object_or_404(Document, id = pdf_id)
        image = pdf.convert_to_image()
        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)        
    