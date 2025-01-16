# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:50:26 2024

@author: roman
"""

import time

def calculate_execution_time(func, *args):
    """
    Calculate and return the time taken for function 'func' to execute with arguments '*args'.
    """
    start_time = time.time()
    return func(*args) - start_time

def func(*args):
    return time.time()

def bubble_sort(nums):
    """
    Sort the list 'nums' using the bubble sort algorithm. Return the sorted list.
    """
    for n in range(len(nums) - 1, 0, -1):
        for i in range(n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

def insertion_sort(nums):
    """
    Sort the list 'nums' using the insertion sort algorithm. Return the sorted list.
    """
    # Return array if less than a sortable amount
    if len(nums) <= 1:
        return nums
 
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
            
    
def fibonacci_recursive(n):
    """
    Return the nth Fibonacci number using a recursive approach.
    """
    # If number is 0 or 1 return 1, else get factorials
    if n == 0 or n == 1: 
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
