def insertion_sort(alist):
    """

    Sort list by insertion algorithm
    """
    for i in range(1, len(alist)):
        j = i - 1
        value = alist.pop(i)
        while (j >= 0) and (alist[j] > value):
            j -= 1
        alist.insert(j + 1, value)
    return alist

if __name__ == '__main__':
    print(insertion_sort([21, 2, 6, 4, 1, 15, 9]))
