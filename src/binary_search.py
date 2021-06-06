def binary_search(list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            right = mid - 1
        elif list[mid] < target:
            left = mid + 1
    else:
        return None


list = [1, 2, 4, 5, 6, 7, 10, 20, 42, 100]
target = 20

res = binary_search(list, target)

print(f"this is your result: ", res)
