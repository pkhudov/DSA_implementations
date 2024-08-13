class CircBufferQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def push(self, item):
        if not self.isEmpty() and self.tail == self.head:
            print('Queue is full, overwriting the oldest item')
            self.head = (self.head + 1) % self.capacity
        self.array[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size = self.size + 1 if self.size < self.capacity else self.size
        
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        item = self.array[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item
    