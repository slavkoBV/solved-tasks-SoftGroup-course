def merge_sort(alist):
    """

    Sort list by merge algorithm
    """
    def merge(a, b):
        result = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        result += a[i:] + b[j:]
        return result

    if len(alist) <= 1:
        return alist
    else:
        left = alist[:len(alist) // 2]
        right = alist[len(alist) // 2:]
    return merge(merge_sort(left), merge_sort(right))


if __name__ == '__main__':
    l = [21, 34, 26, 83, 15, 57, 31, 44, 45, 20]
    print(merge_sort(l))
