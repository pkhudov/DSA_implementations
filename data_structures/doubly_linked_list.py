class Node:
    def __init__(self, data=None, prev=None):
        self.data = data
        self.next = None
        self.prev = prev
    
class Doubly_Linked_List:
    def __init__(self, elements: list = None):
        if elements:
            self.head = Node(elements[0]) 
            self.length = 1
            node = self.head
            for element in elements[1:]:
                node.next = Node(element, node) 
                node = node.next
                self.length += 1
            self.tail = node
        else:
            self.head = Node() #Here, it already starts with a node
            self.tail = self.head
            self.length = 0
        
    def get(self, index):
        if index > self.length - 1 or index < 0:
            raise IndexError("Index out of bounds")
        if index < self.length / 2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length - 1, index, -1):
                node = node.prev
        return node.data

    def set(self, element, index):
        if index > self.length - 1 or index < 0:
            raise IndexError("Index out of bounds")
        if index < self.length / 2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length - 1, index, -1):
                node = node.prev
        node.data = element
    
    def append(self, element):
        if self.head.data is None and self.head.next is None:
            self.head.data = element
            self.tail = self.head
        else:
            self.tail.next = Node(element, self.tail)
            self.tail = self.tail.next
        self.length += 1
    
    def insert(self, element, index):
        if index > self.length or index < 0:
            raise IndexError("Index out of bounds")
        if index == 0:
            new_node = Node(element)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self.length:
            self.append(element)
            return
        elif index < self.length / 2:
            node = self.head
            for _ in range(index-1):
                node = node.next
            new_node = Node(element, node)
            new_node.next = node.next
            node.next.prev = new_node
            node.next = new_node
        else:
            node = self.tail
            for _ in range(self.length, index, -1):
                node = node.prev
            new_node = Node(element, node)
            new_node.next = node.next
            node.next.prev = new_node
            node.next = new_node
        self.length += 1


    def delete(self, index):
        if index > self.length-1 or index < 0:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            if index == self.length - 1:
                self.tail = self.head
        elif index == self.length - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        elif index < self.length / 2:
            node = self.head
            for _ in range(index-1):
                node = node.next
            node.next = node.next.next
            if node.next:
                node.next.prev = node
        else:
            node = self.tail
            for _ in range(self.length, index, -1):
                node = node.prev
            node.next = node.next.next
            if node.next:
                node.next.prev = node
        self.length -= 1

    def traverse_forward(self):
        elements = ['None']
        node = self.head
        while node and node.data is not None:
            elements.append(str(node.data))
            node = node.next
        elements.append('None')
        return '<->'.join(elements)

    def traverse_backward(self):
        elements = ['None']
        node = self.tail
        while node and node.data is not None:
            elements.append(str(node.data))
            node = node.prev
        elements.append('None') 
        return '<->'.join(elements)