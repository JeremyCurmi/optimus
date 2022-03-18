from PIL import Image
from typing import List
from PIL.PngImagePlugin import PngImageFile

def load_image(path: str) -> Image:
    return Image.open(path)

def load_multiple_images(paths: List[str]) -> List[Image]:
    return [load_image(path) for path in paths]

def image_to_pdf_converter(image: PngImageFile) -> Image.Image:
    return image.convert("RGB")

def multiple_images_to_a_pdf_converter(images: List[PngImageFile]) -> List[Image.Image]:
    return [image_to_pdf_converter(i) for i in images]

def save_pdf(image: Image.Image, path:str):
    image.save(path)

def save_multiple_images_in_a_pdf(images: List[Image.Image], path: str):
    im_1 = images[0]
    images.pop(0)
    im_1.save(path, save_all=True, append_images=images)
