from django.urls import path
from .views import *
urlpatterns = [
    path('upload/', view = upload_file ),
]
