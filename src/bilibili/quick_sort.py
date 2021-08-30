def partition(li, left, right):
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= temp:
            left += 1
        li[right] = li[left]
    li[left] = temp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
quick_sort(li, 0, len(li) - 1)
print(li)
