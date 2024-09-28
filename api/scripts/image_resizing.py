import numpy as np
from PIL import Image
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from api.scripts.utility.image_processing_utility import (
    convert_image_to_pixel_array,
    convert_pixel_array_to_image,
    calculate_color_distance,
    orig_image_path,
    corner_test_image_path,
)

tolerance = 30 #default tolerance level for color differences

def get_corner_indices(pixel_array):
    print("Getting corners")
    height, width, _ = pixel_array.shape

    unique_corners = set()

    for r in range(1, height):
        for c in range(1, width):
            corner = (r-1, c-1)

            left_diff = are_colors_different(pixel_array[r-1,c-1], pixel_array[r,c-1])
            top_diff = are_colors_different(pixel_array[r-1,c-1], pixel_array[r-1,c])

            # top left corner
            if top_diff and left_diff:
                if corner not in unique_corners:
                    unique_corners.add(corner)
                continue

            right_diff = are_colors_different(pixel_array[r-1,c], pixel_array[r,c])

            # top right corner
            if top_diff and right_diff:
                if corner not in unique_corners:
                    unique_corners.add(corner)
                continue

            bottom_diff = are_colors_different(pixel_array[r,c-1], pixel_array[r,c])

            # bottom right corner
            if bottom_diff and right_diff:
                if corner not in unique_corners:
                    unique_corners.add(corner)
                continue

            # bottom left corner
            if bottom_diff and left_diff:
                if corner not in unique_corners:
                    unique_corners.add(corner)
                continue
            
    return list(unique_corners)

# sees if colors are considered different based on tolerance
# returns True if they are different, False if they are the same
def are_colors_different(color_a, color_b):
    dist = calculate_color_distance(color_a, color_b)

    return dist > tolerance

def compress_image(image, pixel_size):
    old_height = image.shape[0]
    old_width = image.shape[1]

    new_height = old_height // pixel_size
    new_width = old_width // pixel_size

    print("old height: " + str(old_height) + "   | new height: " + str(new_height))
    print("old width: " + str(old_width) + "   | new height: " + str(new_width))

    new_image_array = np.zeros((new_height, new_width), dtype=image.dtype)

    offset = pixel_size // 2
    
    for row in range(new_height):
        for col in range(new_width):
            new_image_array[row,col] = image[row*pixel_size + offset,col*pixel_size + offset ]

    return new_image_array


def test():
    pixel_array = convert_image_to_pixel_array(orig_image_path)

    corner_list = get_corner_indices(pixel_array)

    print("Marking corners")
    for corner_indices in corner_list:
        r,c = corner_indices
        pixel_array[r,c] = [255,0,255]
        pixel_array[r+1,c] = [255,0,255]
        pixel_array[r,c+1] = [255,0,255]
        pixel_array[r+1,c+1] = [255,0,255]

    convert_pixel_array_to_image(pixel_array, corner_test_image_path)

test()