# ДАСГАЛ 2: In-place Quick Sort (илүү оновчтой)
def partition(arr, low, high):
    """
    Partition функц - массивыг pivot-оор хуваана
    """
    # TODO: Энд кодоо бичнэ үү
    pivot = arr[high]  # Сүүлийн элементийг pivot болгох
    i = low - 1  # Бага элементүүдийн индекс
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_inplace(arr, low=0, high=None):
    """
    In-place Quick Sort - санах ой хэмнэлттэй
    """
    if high is None:
        high = len(arr) - 1
    
    # TODO: Рекурсив нөхцөл
    if low < high:
        # Partition хийх
        pi = partition(arr, low, high)
        
        # Зүүн болон баруун хэсгийг эрэмбэлэх
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)
    
    return arr
