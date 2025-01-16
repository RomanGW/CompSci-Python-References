def merge_sort(arr):
    """
    Sort 'arr' using the merge sort algorithm and return the sorted array.
    """
    
    if len(arr) <= 1:
        return arr
    
    # Get middle point, split arrays, and reform using a sorted version of arrays
    mid = len(arr) // 2
    arr1 = sorted(arr[:mid])
    arr2 = sorted(arr[mid:])
    merged_list = sorted(arr1 + arr2)
    return merged_list

def quick_sort(arr):
    """
    Sort 'arr' using the quick sort algorithm and return the sorted array.
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    less = []
    more = []
    
    for i in arr[:-1]:
        if i < pivot:
            less.append(i)
        else:
            more.append(i)

    return quick_sort(less) + [pivot] + quick_sort(more)
    

def binary_search(arr, x):
    """
    Find 'x' in sorted 'arr' using binary search. Return the index of 'x', or -1 if not found.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1