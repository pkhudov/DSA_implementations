from data_structures.linked_list import LinkedList

class Stack(LinkedList):
    def __init__(self):
        super().__init__()
    
    def push(self, item):
        self.insert(item, 0)
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        item = self.get(0)
        self.delete(0)
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.get(0)

    def is_empty(self):
        return self.length == 0
    
    def size(self):
        return self.length