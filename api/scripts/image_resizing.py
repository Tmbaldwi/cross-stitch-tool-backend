import numpy as np
from collections import Counter
from api.scripts.utility.image_processing_utility import (
    convert_image_to_pixel_array,
    convert_pixel_array_to_image,
    calculate_color_distance,
    orig_image_path,
    corner_test_image_path,
    compressed_original_image_path,
)

COLOR_TOLERANCE = 30 #default tolerance level for color differences
PIXEL_SIZE_OPTIONS_COUNT = 5 # default number of pixel size guesses


def get_corner_indices(pixel_array):
    print("Getting corners")
    height, width, _ = pixel_array.shape

    unique_corners = set()
    corners_by_row = [[] for _ in range(height-1)] #TODO optimize so that it only contains the necessary arrays
    corners_by_column = [[] for _ in range(width-1)] 

    for r in range(1, height):
        for c in range(1, width):
            corner = (r-1, c-1)

            left_diff = are_colors_different(pixel_array[r-1,c-1], pixel_array[r,c-1])
            top_diff = are_colors_different(pixel_array[r-1,c-1], pixel_array[r-1,c])

            # top left corner
            if top_diff and left_diff:
                unique_corners, corners_by_row, corners_by_column = add_corner_to_lists(unique_corners, corners_by_row, corners_by_column, corner)
                continue

            right_diff = are_colors_different(pixel_array[r-1,c], pixel_array[r,c])

            # top right corner
            if top_diff and right_diff:
                unique_corners, corners_by_row, corners_by_column = add_corner_to_lists(unique_corners, corners_by_row, corners_by_column, corner)
                continue

            bottom_diff = are_colors_different(pixel_array[r,c-1], pixel_array[r,c])

            # bottom right corner
            if bottom_diff and right_diff:
                unique_corners, corners_by_row, corners_by_column = add_corner_to_lists(unique_corners, corners_by_row, corners_by_column, corner)
                continue

            # bottom left corner
            if bottom_diff and left_diff:
                unique_corners, corners_by_row, corners_by_column = add_corner_to_lists(unique_corners, corners_by_row, corners_by_column, corner)
                continue

    corners_all = corners_by_row + corners_by_column
    return list(unique_corners), corners_all

def add_corner_to_lists(unique_corners, corners_by_row, corners_by_column, corner):
    if corner not in unique_corners:
        unique_corners.add(corner)
        corners_by_row[corner[0]].append(corner[1])
        corners_by_column[corner[1]].append(corner[0])

    return unique_corners, corners_by_row, corners_by_column


# sees if colors are considered different based on tolerance
# returns True if they are different, False if they are the same
def are_colors_different(color_a, color_b):
    dist = calculate_color_distance(color_a, color_b)

    return dist > COLOR_TOLERANCE

def compress_pixel_array(image_array, pixel_size):
    old_height = image_array.shape[0]
    old_width = image_array.shape[1]

    new_height = old_height // pixel_size
    new_width = old_width // pixel_size

    print("old height: " + str(old_height) + "   | new height: " + str(new_height))
    print("old width: " + str(old_width) + "   | new height: " + str(new_width))

    new_image_array = []

    offset = pixel_size // 2
    
    for row in range(new_height):
        new_image_array.append([])
        for col in range(new_width):
            new_image_array[row].append(image_array[row*pixel_size + offset,col*pixel_size + offset ])

    return new_image_array

def get_pixel_size_options(pixel_array):
    unique_corners, corners_all = get_corner_indices(pixel_array)

    # get counts of distances between each 
    pixel_sizes_by_count = Counter()
    for corner_slice in corners_all:
        if len(corner_slice) == 0:
            continue

        slice_pixel_sizes = np.diff(corner_slice)
        pixel_sizes_by_count.update(slice_pixel_sizes)

    print(pixel_sizes_by_count)

    most_common_sizes = pixel_sizes_by_count.most_common()

    # max_count = most_common_sizes[0][1]
    # smallest_most_common_size = min([element for element, count in most_common_sizes if count == max_count])
    
    return most_common_sizes[:PIXEL_SIZE_OPTIONS_COUNT]


def compress_image_and_return_pixel_sizes(input_path, output_path):
    # read image and convert to pixel array
    pixel_array = convert_image_to_pixel_array(input_path)

    # get pixel size
    print("getting pixel size")
    pixel_size_options = get_pixel_size_options(pixel_array)

    print("Pixel size: " + str(int(pixel_size_options[0][0])))

    # compress image
    print("Compressing image")
    compressed_image = compress_pixel_array(pixel_array, pixel_size_options[0][0])

    # convert pixel array back and write image
    convert_pixel_array_to_image(compressed_image, output_path)

    return pixel_size_options



# testing code ------------------------------------------------------------------------------------------------------
def test():
    # read image and convert to pixel array
    pixel_array = convert_image_to_pixel_array(orig_image_path)

    # get pixel size
    print("getting pixel size")
    pixel_size = get_pixel_size_options(pixel_array)

    print("Pixel size: " + str(int(pixel_size)))

    # compress image
    print("Compressing image")
    compressed_image = compress_pixel_array(pixel_array, pixel_size)

    # convert pixel array back and write image
    convert_pixel_array_to_image(compressed_image, compressed_original_image_path)

def corner_test():
    pixel_array = convert_image_to_pixel_array(orig_image_path)

    corner_list, coners_all = get_corner_indices(pixel_array)

    print("Marking corners")
    for corner_indices in corner_list:
        r,c = corner_indices
        pixel_array[r,c] = [255,0,255]
        pixel_array[r+1,c] = [255,0,255]
        pixel_array[r,c+1] = [255,0,255]
        pixel_array[r+1,c+1] = [255,0,255]

    convert_pixel_array_to_image(pixel_array, corner_test_image_path)
    print("Marking done")