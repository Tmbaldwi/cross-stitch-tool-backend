import os
from PIL import Image
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))

orig_image_path = os.path.join(current_dir, '..', '..', 'media', 'original_image.png')
mod_image_path = os.path.join(current_dir, '..', '..', 'media', 'modified_image.png')

def image_path_valid(image_path):
    if os.path.isfile(image_path):
        print(f"Image file found: {image_path}")
        return True
        
    else:
        print(f"PNG file not found at: {image_path}")
        return False
    
def convert_image_to_pixel_array(image_path):
    try:
        with Image.open(image_path) as image:
            image = image.convert('RGB')
            pixel_array = np.array(image)
            print(f"Image converted to pixel array")
            
            return pixel_array
    except Exception as ex:
        print(f"Error converting image to pixel array: {ex}")
        return None
    
def convert_pixel_array_to_image(pixel_array, output_path):
    try:
        pixel_array = np.array(pixel_array, dtype=np.uint8)
        img = Image.fromarray(pixel_array)
        img.save(output_path)
        print(f"Pixel array converted to image")

        return True
    except Exception as ex:
        print(f"Error converting pixel array to image : {ex}")
        return False

    
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def hex_to_rgb(hex):
    hex_color = hex.lstrip('#')

    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return [r,g,b]