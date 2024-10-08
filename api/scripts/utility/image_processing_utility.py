import os
from PIL import Image
import numpy as np
from typing import Tuple

current_dir = os.path.dirname(os.path.abspath(__file__))

media_dir = os.path.join(current_dir, '..', '..', '..', 'media')

orig_image_path = os.path.join(media_dir, 'original_image.png')
mod_image_path = os.path.join(media_dir, 'modified_image.png')

corner_test_image_path = os.path.join(media_dir, 'corner_test_image.png')
compressed_original_image_path = os.path.join(media_dir, 'original_image_compressed.png')

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


# calculates distance between two colors with simple 3d coordinate distance calculation
def calculate_color_distance(rgb_1: Tuple[int, int, int], rgb_2: Tuple[int, int, int]) -> float:
    # Convert RGB values to float64 first
    rgb_1_int = np.array(rgb_1, dtype=np.int64)
    rgb_2_int = np.array(rgb_2, dtype=np.int64)

    # Calculate squared differences
    red_dist_squared = (rgb_1_int[0] - rgb_2_int[0]) ** 2
    green_dist_squared = (rgb_1_int[1] - rgb_2_int[1]) ** 2
    blue_dist_squared = (rgb_1_int[2] - rgb_2_int[2]) ** 2

    # Return the Euclidean distance as a double (float64)
    return np.sqrt(red_dist_squared + green_dist_squared + blue_dist_squared)