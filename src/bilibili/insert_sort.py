def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        temp = li[i]
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp


li = [1, 20, 23, 42, 21, 19, 10, 13]
insert_sort(li)
print(li)
