class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    break
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key)
                    break
                current = current.right
            else:
                break
    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key 

    def remove(self, key):
        self.root = self._remove_recursive(self.root, key)

    def _remove_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._remove_recursive(node.left, key)
        elif key > node.key:
            node.right = self._remove_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._get_min_node(node.right)
         
            node.key = temp.key
 
            node.right = self._remove_recursive(node.right, temp.key)
      
        return node

    def _get_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current       

class AVL:
    def __init__(self):
        self.root = None

    def build_from_sorted(self, elements):
        self.root = self._build_recursive(elements)

    def _build_recursive(self, elements):
        if not elements:
            return None
        
        mid = len(elements) // 2
        root = Node(elements[mid])
        
        root.left = self._build_recursive(elements[:mid])
        root.right = self._build_recursive(elements[mid+1:])
        
        return root
    
    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key
    
    def remove(self, key):
        self.root = self._remove_recursive(self.root, key)

    def _remove_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._remove_recursive(node.left, key)
        elif key > node.key:
            node.right = self._remove_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._get_min_node(node.right)
         
            node.key = temp.key
 
            node.right = self._remove_recursive(node.right, temp.key)
      
        return node

    def _get_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current