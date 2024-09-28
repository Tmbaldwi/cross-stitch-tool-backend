from api.scripts.thread_color_screen_scrape import get_thread_list
from api.models.color_option_model import ColorOption

from api.scripts.utility.image_processing_utility import (
    hex_to_rgb,
    calculate_color_distance,
)

def get_n_closest_colors(original_color: str, n: int):
    thread_list_unsorted = get_thread_list()
    original_rgb = hex_to_rgb(original_color)

    # loop over all threads and calculate distance
    thread_list_with_score = []
    for thread in thread_list_unsorted:
        score = calculate_color_distance(original_rgb, thread.rgb)
        color_option = ColorOption(thread.name, thread.hex_value)

        thread_list_with_score.append([score, color_option])
    
    # sort by lowest score (closest color)
    thread_list_with_score.sort(key=thread_sort_function)

    # trim score and return only the top n results
    closest_colors = [thread[1] for thread in thread_list_with_score][0:n]

    return closest_colors

def thread_sort_function(pair):
    return pair[0]