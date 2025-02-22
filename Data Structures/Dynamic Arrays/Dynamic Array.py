class DynamicArray:
    def __init__(self):
        self.array = [None] * 1
        self.count = 0
        self.capacity = 1

    def add(self, item):
        """
        Add item to the dynamic array.
        """
        if self.count == self.capacity:
            self._resize(self.capacity * 2)
        
        self.array[self.count] = item
        self.count += 1

    def get(self, index):
        """
        Get the item at the specified index.
        """
        if index < self.count:
            return self.array[index]
        else:
            raise IndexError

    def remove(self, index):
        """
        Remove the item at the specified index.
        """
        if index < self.count:
            # Shift elements to left.
            for i in range(index, self.count - 1):
                self.array[i] = self.array[i + 1]

            # Decrement count.
            self.array[self.count - 1] = None 
            self.count -= 1
            
            # Resize capacity to half of current size.
            if self.count <= self.capacity // 4 and self.capacity > 1:
                self._resize(self.capacity // 2)
        else:
            raise IndexError
    
    def _resize(self, new_capacity):
        """
        Resize the array to the new capacity.
        """
        new_array = [None] * new_capacity

        for i in range(self.count):
            new_array[i] = self.array[i] 
        
        self.array = new_array
        self.capacity = new_capacity