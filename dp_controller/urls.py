from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from .views import *

router.register(r'images', ImagesViewSet, basename='images')
router.register(r'pdfs', DocumentsViewSet, basename='pdfs')

urlpatterns = [
    path('upload/', view = upload_file ),
    path('', include(router.urls)),
    path('rotate/', view = rotate_image),
    path('convert-pdf-to-image/', view = pdf2images)


]
 