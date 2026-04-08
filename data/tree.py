import math

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

    def search(self, key):
        current = self.root
        
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False 

    def rebalance(self):
        if self.root is None:
            return

        pseudo_root = Node(0)
        pseudo_root.right = self.root

        node_count = self._tree_to_vine(pseudo_root)
        self._vine_to_tree(pseudo_root, node_count)

        self.root = pseudo_root.right

    def _tree_to_vine(self, pseudo_root):
        count = 0
        tail = pseudo_root
        rest = tail.right

        while rest is not None:
            if rest.left is None:
                count += 1
                tail = rest
                rest = rest.right
            else:
                temp = rest.left
                rest.left = temp.right
                temp.right = rest
                rest = temp
                tail.right = temp
        return count

    def _vine_to_tree(self, pseudo_root, count):
        leaves = count + 1 - 2**int(math.log2(count + 1))
        self._compress(pseudo_root, leaves)
        
        count = count - leaves
        while count > 1:
            count //= 2
            self._compress(pseudo_root, count)

    def _compress(self, pseudo_root, count):
        scanner = pseudo_root
        for _ in range(count):
            child = scanner.right
            scanner.right = child.right
            scanner = scanner.right
            child.right = scanner.left
            scanner.left = child   

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
    
    def search(self, key):
        current = self.root
        
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False 