def insertion_sort(arr):
    if arr is None:
        return []
    for i in range(1,len(arr)):
        j = i -1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp
    return arr