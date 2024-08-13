class DynamicArray():
    def __init__(self, arg=0):
        # If capacity is provided
        if isinstance(arg, int):
            if arg == 0:
                self.array = [None] * 3
                self.size = 0
                self.capacity = 3
            else:
                self.array = [None] * arg
                self.size = 0
                self.capacity = arg

        # If user provides items
        elif isinstance(arg, list):
            self.array = arg
            self.size = len(arg)
            self.capacity = len(arg)
        else:
            raise(TypeError("Please provide list of items or array capacity"))
        
    def __str__(self):
        return str(self.array[:self.size])

    def __repr__(self):
        return f'DynamicArray({self.array[:self.size]}, size={self.size}, capacity={self.capacity})'
    
    def length(self):
        return self.size

    def set(self, item, index):
        if index > self.size-1 or index < 0:
            raise IndexError("Index out of bounds")
        self.array[index] = item
    
    def get(self, index):
        if index > self.size-1 or index < 0:
            raise IndexError("Index out of bounds")
        return self.array[index]
        
    def insert(self, item, index):
        if index > self.size or index < 0:
            raise IndexError("Index out of bounds")
        
        if self.size == self.capacity: # If capacity reached, augment array
            new_capacity = self.size * 2
            self._resize(new_capacity)
        
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i-1]
    
        self.array[index] = item
        self.size += 1
    
    def delete(self, index):
        if index > self.size-1 or index < 0:
            raise IndexError("Index out of bounds")
        
        for i in range(index, self.size-1):
            self.array[i] = self.array[i+1]

        self.array[self.size-1] = None
        self.size -= 1
    
    def append(self, item):
        self.insert(item, self.size)

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
                new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity