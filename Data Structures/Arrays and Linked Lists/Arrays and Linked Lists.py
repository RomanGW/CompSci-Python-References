def array_sum(arr):
    """
    Calculate and return the sum of elements in an array 'arr'.
    """
    sum = 0
    for element in arr:
        sum += element
    return sum

def find_middle_node(linked_list):
    """
    Find and return the middle node of a singly linked list.
    If the list has an even number of nodes, return the second middle node.
    """
    # For some reason it keeps giving me a "ListNode is not defined" error.
    # ListNode is mentioned in tester and tests but not written in the assignment guide.
    # So I am going to assume that this is a test with either tester.py or tests.py.
    
    slow = linked_list
    fast = linked_list

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

def remove_duplicates_from_sorted_array(arr):
    """
    Given a sorted array, remove the duplicates in-place such that each element appears only once.
    Return the new length of the array.
    """
    
    if not arr:
        return 0

    write_index = 1
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1

    return write_index

