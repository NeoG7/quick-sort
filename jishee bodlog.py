def quick_sort(arr):
#     quick_sort() нэртэй функц үүсгэж байна.
# Оролт нь arr (массив).
    if len(arr) <= 1:
        return arr
# Массивын урт 1 эсвэл 0 байвал ямар ч эрэмбэлэлт хэрэггүй.
# Жишээ нь [3], [] бол шууд буцаана.
# Гэхдээ манай жишээнд len(arr) = 7 тул энэ нөхцөл биелэхгүй → дараагийн мөр рүү орно.
    pivot = arr[len(arr) // 2]
# Pivot гэдэг нь “тулгуур” элемент.

# Массивын дундаас len(arr) // 2 (integer division) ашиглан нэг элементийг сонгож байна.

# Жишээ нь arr = [8, 3, 1, 7, 0, 10, 2] →
# len(arr) = 7, тэгэхээр arr[7//2] = arr[3] = 7
# Тэгэхээр pivot = 7
    left = [x for x in arr if x < pivot]
# Энэ мөр List Comprehension ашиглан массивын pivot-оос бага бүх элементүүдийг left хэсэгт авна.
# Жишээ нь arr = [8, 3, 1, 7, 0, 10, 2] →
# left = [3, 1, 0, 2]
    right = [x for x in arr if x > pivot]
# Энэ мөр List Comprehension ашиглан массивын pivot-оос их бүх элементүүдийг right хэсэгт авна.
# Жишээ нь arr = [8, 3, 1, 7, 0, 10, 2] →
# right = [8, 10]
    return quick_sort(left) + [pivot] + quick_sort(right)
# Энэ нь рекурсийн задаргаа.
# left болон right хэсэгтэй тооцоог хийнэ.
# left болон right хэсэгтэй тооцоог хийнэ.
arr = [8, 3, 1, 7, 0, 10, 2]
print(quick_sort(arr))