import random

# every out loop bubble the maxizm data


def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


li = [random.randint(0, 10000) for i in range(100)]
print(li, '\n--------------------------')
bubble_sort(li)
print(li)


# impolve
def bubble_sort_advance(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len[li] - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            break


li_advance = [random.randint(0, 10000) for i in range(100)]
print(li_advance, '\n--------------------------')
bubble_sort(li_advance)
print(li_advance)
