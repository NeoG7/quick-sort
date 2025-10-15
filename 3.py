
# ДАСГАЛ 3: Random Pivot Quick Sort (муу тохиолдлоос зайлсхийх)
import random

def partition_random(arr, low, high):
    """
    Санамсаргүй pivot сонгох partition
    """
    # TODO: Санамсаргүй индекс сонгож pivot болгох
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    
    return partition(arr, low, high)


def quick_sort_random(arr, low=0, high=None):
    """
    Санамсаргүй pivot ашигласан Quick Sort
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition_random(arr, low, high)
        quick_sort_random(arr, low, pi - 1)
        quick_sort_random(arr, pi + 1, high)
    
    return arr