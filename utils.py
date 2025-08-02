from pdf2image import convert_from_path
from PIL import Image
import os

def pdf_to_images(pdf_path, output_folder="temp_images"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    images = convert_from_path(pdf_path)
    image_paths = []
    for i, img in enumerate(images):
        path = os.path.join(output_folder, f"page_{i}.png")
        img.save(path, 'PNG')
        image_paths.append(path)
    return image_paths
