def partition(arr, low, high):
    part_idx = low
    for i in range(low, high):
        if arr[i] < arr[high]: # here element at high index is treated as pivot
            arr[i], arr[part_idx] = arr[part_idx], arr[i]
            part_idx += 1
    arr[part_idx], arr[high] = arr[high], arr[part_idx]
    return part_idx

def _quick_sort(arr, low, high):
    if low < high:
        part_idx = partition(arr, low, high)
        # at this point element at partition index is at right place

        _quick_sort(arr, low, part_idx - 1)
        _quick_sort(arr, part_idx + 1, high)

def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)
    return arr

if __name__ == '__main__':
    arr = [1,9,4,8,6,2,5,7,3]
    quick_sort(arr)
    print(arr) # in-place sorting