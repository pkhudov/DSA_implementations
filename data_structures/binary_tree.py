class Node:
    def __init__(self, item, parent=None):
        self.item = item
        self.parent = parent
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, item):
        if not self.root:
            self.root = Node(item)
        else:
            self._insert(self.root, item)

    def insert_iterative(self, item):
        node = self.root
        parent = None
        while node:
            parent = node
            if item < node.item:
                node = node.left
            else: node = node.right

        if not parent:
            self.root = Node(item, parent)
        elif item < parent.item:
            parent.left = Node(item, parent)
        else:
            parent.right = Node(item, parent)

    def tree_walk(self):
        tree_repr = []
        return self._in_order_tree_walk(self.root, tree_repr)
    
    def search(self, item):
        return self._search(self.root, item)
    
    def min(self):
        return self._min(self.root)
    
    def max(self):
        return self._max(self.root)
    
    def successor(self, node):
        if node.right:
            return self._min(node.right)
        else:
            anc = node.parent
            while anc and node == anc.right:
                node = anc
                anc = anc.parent
            return anc
        
    def predecessor(self, node):
        if node.left:
            return self._max(node.left)
        else:
            anc = node.parent
            while anc and node == anc.left:
                node = anc
                anc = anc.parent
            return anc
        
    def delete(self, node):
        if not node.left:
            self._transplant(node, node.right)
        elif not node.right:
            self._transplant(node, node.left)
        else:
            successor = self._min(node.right) # The only O(h) operation
            if successor != node.right:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def _insert(self, node, item):
        if item < node.item:
            if node.left:
                self._insert(node.left, item)
            else:
                node.left = Node(item, node)
        else:
            if node.right:
                self._insert(node.right, item)
            else:
                node.right = Node(item, node)
                
    def _in_order_tree_walk(self, node, tree_repr):
        if node:
            self._in_order_tree_walk(node.left, tree_repr)
            tree_repr.append(node.item)
            self._in_order_tree_walk(node.right, tree_repr)
        return tree_repr
    
    def _search(self, node, item):
        # if not node or node.item == item:
        #     return node
        # else:
        #     if item < node.item:
        #         return self._search(node.left, item)
        #     else:
        #         return self._search(node.right, item)
        while node and node.item != item:
            if item < node.item:
                node = node.left
            else:
                node = node.right
        return node
    
    def _min(self, node):
        while node:
            node = node.left
        return node
    
    def _max(self, node):
        while node:
            node = node.right
        return node
    
    def _transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else: u.parent.right = v
        if v:
            v.parent = u.parent

   
# tree = BST()
# tree.insert(2)
# tree.insert(5)
# tree.insert(5)
# tree.insert(6)
# tree.insert(9)
# tree.insert(7)
# tree.insert(8)
# print(tree.tree_walk())
# print(tree.search(7))
# node = tree.search(6)
# tree.delete(node)
# print(tree.tree_walk())