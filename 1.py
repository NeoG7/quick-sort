# ДАСГАЛ 1: Энгийн Quick Sort (Lomuto Partition)
# Та доорх функцийг бөглө
def quick_sort_basic(arr):
    """
    Энгийн Quick Sort алгоритм
    """
    # TODO: Эндээс эхлээрэй
    # Хэрэв массив хоосон эсвэл 1 элементтэй бол буцаах
    if len(arr) <= 1:
        return arr
    
    # Pivot сонгох (сүүлийн элемент)
    pivot = arr[-1]
    
    # Бага, тэнцүү, их гэсэн 3 жагсаалт үүсгэх
    less = []
    equal = []
    greater = []
    
    # TODO: Элемент бүрийг харьцуулж хуваах
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
    
    # Рекурсив дуудах
    return quick_sort_basic(less) + equal + quick_sort_basic(greater)