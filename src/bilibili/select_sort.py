def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i+1, len(li) - 1):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]


li = [10, 20, 3, 1, 34, 4, 98]
select_sort(li)
print(li)
