import argparse
from PIL import Image
from typing import List
from PIL.PngImagePlugin import PngImageFile

def load_image(path: str) -> Image.Image:
    return Image.open(path)

def load_multiple_images(paths: List[str]) -> List[Image.Image]:
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

def main(image_paths: list, pdf_paths: list):
    if len(image_paths) == len(pdf_paths):
        for i,p in zip(image_paths,pdf_paths):
            im = load_image(i)
            im_conv = image_to_pdf_converter(im)
            save_pdf(im_conv, p)
    elif (len(image_paths) > len(pdf_paths)) and (len(pdf_paths) == 1):
        images = load_multiple_images(image_paths)
        images_conv = multiple_images_to_a_pdf_converter(images)
        save_multiple_images_in_a_pdf(images_conv, pdf_paths[0])
    else:
        raise Exception("Not yet Implemented!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="convert images to pdf")
    parser.add_argument("--image", type=str, required=True, help="path to image", nargs="+")
    parser.add_argument("--pdf", type=str, required=True, help="path to exported pdf", nargs="+")

    args = parser.parse_args()
    main(args.image, args.pdf)