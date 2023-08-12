from base64 import b64decode
from django.core.files.base import ContentFile
import string
import random


def b64_to_pdf(b64):
    decoded_data = b64decode(b64, validate=True)
    file_name = generate_random_filename(10)
    data = ContentFile(decoded_data, name=file_name)
    return data


def generate_random_filename(length):
    letters = string.ascii_lowercase + string.ascii_uppercase
    return "".join(random.choice(letters) for _ in range(length)) + ".pdf"
 