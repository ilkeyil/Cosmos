from io import BytesIO

from django.core.files import File
from PIL import Image


def compress(image):
    img = Image.open(image)
    img_io = BytesIO()
    img.save(img_io, "JPEG", optimize=True, quality=85)
    compressed_img = File(img_io, name=image.name)
    return compressed_img
