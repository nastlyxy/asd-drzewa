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