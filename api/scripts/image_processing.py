import os
from PIL import Image
import numpy as np

orig_image_path = 'media/original_image.png'
mod_image_path = 'media/modified_image.png'

tolerance = 5 #TODO add tolerance to images

def get_color_palette_from_image(image_path):
    # check image exists and path is valid
    if not image_path_valid(image_path):
        return None
    
    # take image and convert to a pixel array
    pixels = convert_image_to_pixel_array(image_path)
    
    # get color palette
    palette = process_image_for_color_palette(pixels)
    
    return palette


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
    
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
    
def process_image_for_color_palette(pixel_array):
    height, width, _ = pixel_array.shape
    unique_colors = []
    colors_seen = set()

    for col in range(width):
        for row in range(height):
            pixel = pixel_array[row,col]
            color_hex = rgb_to_hex(pixel)
            
            if color_hex not in colors_seen:
                unique_colors.append(color_hex)
                colors_seen.add(color_hex)
    
    print(f"Unique colors found: {len(unique_colors)}")

    return unique_colors

get_color_palette_from_image(orig_image_path)
