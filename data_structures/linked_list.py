class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, items: list = None):
        self.head = None
        self.length = 0
        if items:
            for item in items:
                self.append(item)
        
    def __str__(self):
        return self.traverse()
    
    def get(self, index):
        if index > self.length-1 or index < 0:
            raise IndexError("Index out of bounds")
        node = self.head
        for _ in range(index):
            node = node.next
        return node.data

    def set(self, item, index):
        if index > self.length-1 or index < 0:
            raise IndexError("Index out of bounds")
        node = self.head
        for _ in range(index):
            node = node.next
        node.data = item

    def insert(self, item, index):
        if index > self.length or index < 0:
            raise IndexError("Index out of bounds")
        new_node = Node(item)
        if index == 0:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node
        self.length += 1

    def delete(self, index):
        if index > self.length-1 or index < 0:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            node.next = node.next.next
        self.length -= 1

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next = new_node
        self.length += 1

    def traverse(self):
        node = self.head
        items = []
        while node is not None:
            items.append(str(node.data))
            node = node.next
        items.append('None')
        return '->'.join(items)


# list = LinkedList([1,2,3])
# print(list.head.data)
# print(list.head.next.data)
# print(list.head.next.next.data)
# print("----")
# list.set(99, 2)
# list.insert(23, 0)
# print(list.head.data)
# print(list.head.next.data)
# print(list.head.next.next.data)
# print(list.head.next.next.next.data)
# print(list)
# print(list.length)

# list2 = LinkedList()
# print(list2)
# list3 = LinkedList([1,2,3])
# list3.delete(0)
# print(list3)