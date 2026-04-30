import math


class binary_heap:

    def __init__(self):
        self.heap = [0]

    def get_min(self):
        if len(self.heap) <= 1:
            print("No heap yet...")
            return
        else:
            return self.heap[1]
    
    def insert(self, val:int):

        if len(self.heap) <= 1:
            self.heap.append(val)
            return 1
        
        self.heap.append(val)
        i = len(self.heap) - 1

        while self.heap[(i//2)] > self.heap[i]:
            tmp = self.heap[(i//2)]
            self.heap[(i//2)] = self.heap[i]
            self.heap[i] = tmp
            i = i//2
    
    def delete_i(self, i:int):
        if len(self.heap) <= 1:
            print ("No heap yet...")
            return 
        self.heap[i] = self.heap.pop()

        while 2*i < len(self.heap):
            l = self.heap[2*i]
            r = self.heap[2*i + 1]

            if l <= r and l < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i*2]
                self.heap[i*2] = tmp
                i = i*2
            
            if l > r and r < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i*2 + 1]
                self.heap[i*2 + 1] = tmp
                i = i*2 + 1
            

            
    
h = binary_heap()
h.insert(5)
h.insert(10)
h.insert(3)
h.insert(1)
h.insert(4)
h.insert(6)
print(h.heap)
print(h.get_min())
h.delete_i(1)
print(h.heap)

'''

        0
        1
       / \
      3   5
     / \
    10  4
'''