def selection_sort(nums):
    """
    Implement the selection sort algorithm to sort the list 'nums' in ascending order.
    Return the sorted list.
    """
    n = len(nums)
    for i in range(n - 1):
        min_val = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_val]:
                min_val = j
        nums[i], nums[min_val] = nums[min_val], nums[i]
    return nums

def quick_sort(arr):
    """
    Implement the quick sort algorithm to sort the list 'arr' in ascending order.
    Return the sorted list.
    """
    if len(arr) <= 1:
        return arr
    
    # Choosing a pivot element
    pivot = arr[len(arr) // 2]
    
    # Partitioning
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    more = [x for x in arr if x > pivot]
    
    return quick_sort(less) + equal + quick_sort(more)
    
def binary_search_first_occurrence(arr, x):
    """
    Implement a variation of binary search to find the first occurrence of 'x' in the sorted list 'arr'.
    Return the index of the first occurrence of 'x'. If 'x' is not present in 'arr', return -1.
    """
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            result = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return result
