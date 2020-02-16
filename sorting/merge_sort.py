def merge(arr1, arr2):
    res_arr = []
    i = j = 0
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1 + arr2
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res_arr.append(arr1[i])
            i += 1
        else:
            res_arr.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        res_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        res_arr.append(arr2[j])
        j += 1
    return res_arr

def _merge_sort(arr, i, j):
    if i == j or i > j:
        return [arr[j]]
    mid = (i + j) // 2

    # break the sorting work into two parts at every step and then merge the results
    return merge(_merge_sort(arr, i, mid), _merge_sort(arr, mid + 1, j))

def merge_sort(arr):
    return _merge_sort(arr, 0, len(arr)-1)

print(merge_sort([1,3,4,5,6,2,7,58,9,45]))
