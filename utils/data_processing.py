import os
from unstructured.partition.pdf import partition_pdf
import base64
from utils.config import INPUT_PATH, OUTPUT_PATH

def extract_pdf_elements(filename):
    raw_pdf_elements = partition_pdf(
        filename=os.path.join(INPUT_PATH, filename),
        extract_images_in_pdf=True,
        infer_table_structure=True,
        chunking_strategy="by_title",
    )

    text_elements, table_elements, image_elements = [], [], []
    for element in raw_pdf_elements:
        if 'CompositeElement' in str(type(element)):
            text_elements.append(element.text)
        elif 'Table' in str(type(element)):
            table_elements.append(element.text)

    # Save and encode images
    image_elements = []
    for image_file in os.listdir(OUTPUT_PATH):
        if image_file.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(OUTPUT_PATH, image_file)
            image_elements.append(encode_images(image_path))
    
    return text_elements, table_elements, image_elements

def encode_images(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
