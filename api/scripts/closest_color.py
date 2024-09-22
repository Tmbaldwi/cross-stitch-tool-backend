from api.scripts.thread_color_screen_scrape import get_thread_list
from api.scripts.image_processing_utility import hex_to_rgb
from typing import Tuple
import math

def get_n_closest_colors(original_color: str, n: int):
    thread_list_unsorted = get_thread_list()
    original_rgb = hex_to_rgb(original_color)

    thread_list_with_score = []
    for thread in thread_list_unsorted:
        score = calculate_color_distance(original_rgb, thread.rgb)

        thread_list_with_score.append([score, thread])

    thread_list_with_score.sort(key=thread_sort_function)

    return thread_list_with_score[0:n]

def thread_sort_function(pair):
    return pair[0]

def calculate_color_distance(rgb_1: Tuple[int, int, int], rgb_2: Tuple[int, int, int]):

    red_dist_squared = (rgb_1[0] - rgb_2[0])**2
    green_dist_squared = (rgb_1[1] - rgb_2[1])**2
    blue_dist_squared = (rgb_1[2] - rgb_2[2])**2

    return math.sqrt(red_dist_squared + green_dist_squared + blue_dist_squared)