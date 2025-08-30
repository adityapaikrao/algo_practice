class MinHeap:
    """
    MinHeap. Support insert(value), extractMin(), getTop(), size(), isEmpty(), changeKey(idx, value)
    """
    def __init__(self, arr = None):
        if arr is None:
            self.heap = []
        else:
            self.heap = arr[:]
            for i in range((len(self.heap))//2 -1, -1, -1):
                self.__heapify_down(i)

    def __parent(self, idx):
        return (idx - 1) // 2
    
    def __left_child(self, idx):
        return 2 * idx + 1
    
    def __right_child(self, idx):
        return 2 * idx + 2
    
    def __heapify_up(self, idx = None):
        idx = len(self.heap) - 1 if idx is None else idx
        while idx > 0:
            parent_idx = self.__parent(idx)
            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break
        return

    def __heapify_down(self, idx = None):
        idx = 0 if idx is None else idx
        while idx < len(self.heap):
            left_child_idx = self.__left_child(idx)
            right_child_idx = self.__right_child(idx)

            smallest_idx = idx
            if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[smallest_idx]:
                smallest_idx = left_child_idx
            
            if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[smallest_idx]:
                smallest_idx = right_child_idx
            
            if smallest_idx == idx: 
                break
            else:
                self.heap[smallest_idx], self.heap[idx] = self.heap[idx], self.heap[smallest_idx]
                idx = smallest_idx
        return
    
     
    def insert(self, value):
        self.heap.append(value)
        self.__heapify_up()

        return
        
    def extractMin(self):
        if not self.heap: return None

        self.heap[0], self.heap[-1]  = self.heap[-1], self.heap[0]
        min_val = self.heap.pop()

        self.__heapify_down()

        return min_val

    def getTop(self):
        return self.heap[0] if self.heap else None
    
    def changeKey(self, idx, value):
        if value == self.heap[idx]: 
            return

        elif value < self.heap[idx]:
            self.heap[idx] = value
            self.__heapify_up(idx)
        
        else:
            self.heap[idx] = value
            self.__heapify_down(idx)

        return
    
    def size(self):
        return len(self.heap)
    
    def isEmpty(self):
        return len(self.heap) == 0
    


                
