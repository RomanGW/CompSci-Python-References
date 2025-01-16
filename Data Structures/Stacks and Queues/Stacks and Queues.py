class QueueUsingStacks:
    """
    A queue implementation using two stacks.
    """
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop() if self.out_stack else None

def validate_brackets(string):
    """
    Check if the brackets in the given string are balanced.
    Returns True if balanced, False otherwise.
    """
    stack = []
    # Mapping of closing and opening brackets
    brackets = {'}': '{', ')': '(', ']': '['}
    
    for char in string:
        # Check for opening brackets in string using brackets keys
        if char in brackets.values(): 
            stack.append(char)
        # Check for closing brackets in string using brackets values
        elif char in brackets.keys():
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop() 
    
    # If stack is empty, all brackets matched
    if not stack:
        return True
    return False


def next_greater_element(nums):
    """
    Given a list of numbers, for each element find the next greater element and return their list.
    If no greater element exists for an element, use -1 instead.
    """
    result = []
    for num in nums:
        result.append(-1)
    stack = []
    
    for index, i in enumerate(nums):
        while stack and nums[stack[-1]] < i:
            result[stack.pop()] = i
        stack.append(index)
    
    return result

# Add a third function here for the students to implement
def reverse_stack(stack):
    """
    Reverse the given stack using only push and pop operations.
    The function should return the reversed stack.
    """
    auxiliary_stack = []
    
    while stack:
        element = stack.pop()
        auxiliary_stack.append(element)
    
    return auxiliary_stack
