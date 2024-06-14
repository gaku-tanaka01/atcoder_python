def binary_search(sorted_array, target):
    left = 0
    right = len(sorted_array)-1

    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
