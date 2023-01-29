# Challenge Summary
Merge sort is a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.

In simple terms, we can say that the process of merge sort is to divide the array into two halves, sort each half, and then merge the sorted halves back together. This process is repeated until the entire array is sorted.
- Source: [geeksforgeeks](https://www.geeksforgeeks.org/merge-sort/)

## Whiteboard Process
![Merge Sort](sorting/merge/merge_sort.png)

## Efficiency
- Big O Time: O(n*log n)
- Big O Space: O(n)

## Solution
```
def merge_sort(arr):
    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)

    return arr

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        arr[k:] = right[j:]
    else:
        arr[k:] = left[i:]

    return arr
```
