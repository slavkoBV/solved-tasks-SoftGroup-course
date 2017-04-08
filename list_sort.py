def select_sort(alist):
    """

    Алгоритм сортування вибором
    """

    list_sort = []
    while len(alist):
        for x in alist:
            if x == min(alist):
                list_sort.append(x)
                alist.remove(x)
    return list_sort


l = [5, 6, 21, 1, 2, 1, 15, 3, 7, 16]
print('select ', select_sort(l))


def bubble_sort(alist):
    """

    Алгоритм сортування бульбашкою
    pass_number --> кількість проходів + 1 =
    = кількість елементів - 2
    """
    for pass_number in range(len(alist) - 1, 0, -1):
        for i in range(pass_number):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist


l = [5, 6, 1, 21, 1, 2, 15, 3, 7, 16]
print('bubble ', bubble_sort(l))


def insertion_sort(alist):
    """
    Алгоритм сортування вставкою
    """

    for i in range(1, len(alist)):
        j = i - 1
        value = alist.pop(i)
        while (j >= 0) and (alist[j] > value):
            j -= 1
        alist.insert(j + 1, value)
    return alist


l = [5, 6, 1, 21, 1, 2, 15, 3, 7, 16]
print('insertion1 ', insertion_sort(l))


# Insertion sorting algorithm second realization
def insertion_sort2(alist):
    for i in range(1, len(alist)):
        while i > 0 and alist[i] < alist[i - 1]:
            alist[i], alist[i - 1] = alist[i - 1], alist[i]
            i -= 1
    return alist


l = [5, 6, 1, 21, 1, 2, 15, 3, 7, 16]
print('insertion2 ', insertion_sort2(l))


def qsort(alist):
    if alist:
        return qsort([x for x in alist if x < alist[0]]) + [x for x in alist if x == alist[0]] + qsort([x for x in alist if x > alist[0]])
    return []


l = [5, 6, 1, 21, 1, 2, 15, 3, 7, 16]
print('quicksort ', qsort(l))
