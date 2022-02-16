def partition(array: list, start: int, end: int) -> int:
    """
    Функция сортировки.
    Возвращает индекс граничного элемента.
    """
    idx_left, idx_right = start, end - 1
    pivot = array[(end + start) // 2]
    while True:
        while array[idx_left] < pivot:
            idx_left += 1
        while pivot < array[idx_right]:
            idx_right -= 1
        if idx_left > idx_right - 1:
            break
        array[idx_left], array[idx_right] = array[idx_right], array[idx_left]
        idx_left += 1
        idx_right -= 1

    return idx_left


def quicksort(array, start: int, end: int) -> None:
    """
    Функция запуска сортировки в разных частях массива.
    Работает пока длина массива не будет равна 1.
    :param start: 0 (индекс 1-го элемента массива)
    :param end: длина массива
    """
    if end - start == 1:
        return
    else:
        center = partition(array, start, end)
        quicksort(array, start, center)
        quicksort(array, center, end)
