def select_sort(alist):
    """

    Sort list by selection algorithm
    """

    list_sort = []
    while len(alist):
        for x in alist:
            if x == min(alist):
                list_sort.append(x)
                alist.remove(x)
    return list_sort


if __name__ == '__main__':
    l = [5, 6, 21, 1, 2, 1, 15, 3, 7, 16]
    print(select_sort(l))
