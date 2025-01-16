class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)

        # Bubble up.
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        
        # Swap and pop.
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_element = self.heap.pop()

        # Bubble down 
        index = 0
        while (2 * index + 1) < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest_index = index
            
            # Thank you https://www.programiz.com/dsa/heap-data-structure
            if self.heap[left_child_index] < self.heap[smallest_index]:
                smallest_index = left_child_index
            
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest_index]:
                smallest_index = right_child_index
            
            if smallest_index != index:
                self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
                index = smallest_index
            else:
                break
        
        return min_element

    def get_min(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None