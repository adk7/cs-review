import operator


class Heap(object):
    """
    Attributes:
        heap: List representation of a heap]
        compare(p, c): comparator function returns True if the relations between p, c is parent - child
    """
    
    def __init__(self, heap=None, compare=operator.lt):
        
        self.compare = compare 
        if not heap:
            self.heap = []
        else:
            self.heap = heap
            self.heapify(len(heap) - 1)
            
    def __repr__(self):
        return 'Heap({}, {})'.format(self.heap, self.compare)
    
    def __len__(self):
        return len(self.heap)
           
    def heapify(self, end_index):
             
        child_index = end_index
        parent_index = (child_index - 1) // 2
        
        while parent_index >= 0:
            self._percolate_down(parent_index, end_index)
            parent_index -= 1
        
                    
    def _siftup(self, child_index):
        """
        Heapify starting from bottom
        """
        heap, compare = self.heap, self.compare
        child = child_index
        
        while child > 0:
            parent = (child - 1)//2
            if compare(heap[parent], heap[child]):
                return
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
            
    def _siftdown(self, parent_index):
        """
        Heapify from top
        """
        heap, compare = self.heap, self.compare
        parent = parent_index
        length = len(self.heap)
        
        while (parent * 2) + 1 < length:
            child = (parent * 2) + 1
            if child + 1 < length and compare(heap[child + 1], heap[child]):
                child += 1
            if compare(heap[parent], heap[child]):
                return
            
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
    
    
    def _percolate_down(self, index, end_index):
        left = self._get_left_child_index(index, end_index)
        right = self._get_right_child_index(index, end_index)                                    
        heap = self.heap        
        compare = self.compare
        
        if left != -1 and compare(heap[left], heap[index]):
            heap[left], heap[index] = heap[index], heap[left]
            self._percolate_down(left, end_index)
        
        if right != -1 and compare(heap[right], heap[index]):
            heap[right], heap[index] = heap[index], heap[right]
            self._percolate_down(right, end_index)
                
    def sort(self):
        heap = self.heap
        end_index = len(heap) - 1
        
        while end_index > 0:
            heap[0], heap[end_index] = heap[end_index], heap[0]
            end_index -= 1
            self._percolate_down(0, end_index)
            
    @staticmethod
    def _get_left_child_index(index, end_index):
        left_child_index = (index * 2) + 1
        if left_child_index > end_index:
            return -1
        
        return left_child_index
    @staticmethod    
    def _get_right_child_index(index, end_index):
        right_child_index = (index * 2) + 2
        if right_child_index > end_index:
            return -1
        
        return right_child_index
    
    
class MinHeap(Heap):
    
    
    def __init__(self, heap=None, compare=operator.lt):
        super().__init__(heap, compare)
        
    def insert(self, value):
        self.heap.append(value)
        self._siftup(len(self.heap) -1)
                
    def pop_min(self):
        min_value = self.heap[0]
        
        if len(self.heap) > 1: 
            self.heap[0] = self.heap.pop() # this doesnt work when there is only one element in the heap
            self._siftdown(0)
        else:
            self.heap.pop()
            
        return min_value
        
        
class MaxHeap(Heap):
    
    def __init__(self, heap=None, compare=operator.gt):
        super().__init__(heap, compare)
        
    def insert(self, value):
        self.heap.append(value)
        self._siftup(len(self.heap) -1)
                
    def pop_max(self):
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._siftdown(0)
        return min_value    

            
def heap_sort(items):
    
    heap = MaxHeap(items)
    heap.sort()
    
    return heap.heap
    
    
def max_element(min_heap):
    """
    return the max element in a min heap
    """
    heap = min_heap.heap
    last_index = len(min_heap) - 1
    last_parent = (last_index - 1)//2
    
    first_child = last_parent + 1
    
    #print("children nodes are {}".format((min_heap.heap[first_child:]))) 
    max_value = heap[first_child]
    
    for i in range(first_child, last_index + 1):
        if heap[i] > max_value:
            max_value = heap[i]
            
    return max_value
    

def compare(p, c):
    return p[0] < c[0]
    
def merge_k_sorted_lists(k_sorted_lists):
    """
    Given K sorted lists, merge them together to return one sorted list
    """
    min_heap = MinHeap([], compare)
    k = len(k_sorted_lists)
    total_elements = sum(len(row) for row in k_sorted_lists)
    final_sorted_list = list()
    
    for i in range(k):
        element = (k_sorted_lists[i].pop(0), i)
        min_heap.insert(element)
    
    for i in range(total_elements):
        print(min_heap)
        min_value = min_heap.pop_min()
        final_sorted_list.append(min_value[0])
        index = min_value[1]
        print(final_sorted_list)
        if len(k_sorted_lists[index]) > 0:
            min_heap.insert((k_sorted_lists[index].pop(0), index))
    
    return final_sorted_list