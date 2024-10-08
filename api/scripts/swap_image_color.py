from api.scripts.utility.image_processing_utility import (
    image_path_valid,
    convert_image_to_pixel_array,
    convert_pixel_array_to_image,
    rgb_to_hex,
    hex_to_rgb,
)

def swap_image_color(originalColor, newColor, reference_image_path, modified_image_path):
    # check image exists and path is valid
    if not image_path_valid(reference_image_path) or not image_path_valid(modified_image_path):
        return False
    
    # convert both images to pixel arrays
    orig_image_array = convert_image_to_pixel_array(reference_image_path)
    mod_image_array = convert_image_to_pixel_array(modified_image_path)

    if orig_image_array is None or mod_image_array is None:
        return False

    height, width, _ = orig_image_array.shape
    newColor_rgb = hex_to_rgb(newColor)

    # loop over original image, everytime color is seen swap it on the new image
    for col in range(width):
        for row in range(height):
            if rgb_to_hex(orig_image_array[row,col]) == originalColor:
                mod_image_array[row,col] = newColor_rgb

    return convert_pixel_array_to_image(mod_image_array, modified_image_path)
 