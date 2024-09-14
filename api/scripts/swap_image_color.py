import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from api.scripts.image_processing_utility import (
    image_path_valid,
    convert_image_to_pixel_array,
    convert_pixel_array_to_image,
    rgb_to_hex,
    hex_to_rgb,
    orig_image_path,
    mod_image_path,
)

def swap_image_color(originalColor, newColor):
    # check image exists and path is valid
    if not image_path_valid(orig_image_path) or not image_path_valid(mod_image_path):
        return False
    
    # convert both images to pixel arrays
    orig_image_array = convert_image_to_pixel_array(orig_image_path)
    mod_image_array = convert_image_to_pixel_array(mod_image_path)

    if orig_image_array is None or mod_image_array is None:
        return False

    height, width, _ = orig_image_array.shape
    newColor_rgb = hex_to_rgb(newColor)

    # loop over original image, everytime color is seen swap it on the new image
    for col in range(width):
        for row in range(height):
            if rgb_to_hex(orig_image_array[row,col]) == originalColor:
                mod_image_array[row,col] = newColor_rgb

    return convert_pixel_array_to_image(mod_image_array, mod_image_path)
 