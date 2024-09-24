from api.scripts.utility.image_processing_utility import image_path_valid, convert_image_to_pixel_array, rgb_to_hex, orig_image_path
from api.scripts.closest_color import get_n_closest_colors
from api.models.palette_model import Palette

num_colors_returned = 5 #TODO add choice

def get_palette_and_closest_colors():
    image_colors = get_color_palette_from_original_image()

    # get the 'num_colors_returned' closest colors to a given image color
    palette = []
    for color in image_colors:
        color_options = get_n_closest_colors(color, num_colors_returned)
        palette.append(Palette(color, color_options))
    
    return image_colors, palette



def get_color_palette_from_original_image():
    # check image exists and path is valid
    if not image_path_valid(orig_image_path):
        return None
    
    # take image and convert to a pixel array
    pixels = convert_image_to_pixel_array(orig_image_path)
    
    # get color palette
    palette = process_image_for_color_palette(pixels)
    
    return palette

def process_image_for_color_palette(pixel_array):
    height, width, _ = pixel_array.shape
    unique_colors = []
    colors_seen = set()

    # create list of unique colors from the image
    for col in range(width):
        for row in range(height):
            pixel = pixel_array[row,col]
            color_hex = rgb_to_hex(pixel)
            
            if color_hex not in colors_seen:
                unique_colors.append(color_hex)
                colors_seen.add(color_hex)
    
    print(f"Unique colors found: {len(unique_colors)}")

    return unique_colors