def insert_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        key = list[i]
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


list = [12, 1, 30, 30, 4]
insert_sort(list)
print(list)
