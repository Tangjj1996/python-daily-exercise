def sift(li, low, high):
    """
    :param li:
    :param low:
    :param high:
    :return:
    """
    i = low
    j = 2 * i + 1
    tmp = li[i]
    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:
            j += 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    else:
        li[i] = tmp


def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)


list = [10, 20, 20, 40, 4, 50, 39, 30, 20]
heap_sort(list)
print(list)
