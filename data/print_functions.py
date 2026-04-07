#tutaj będa funkcje dla komendy print
from tree import BST, AVL
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def get_preorder( node, result):
    if node:
        result.append(str(node.key))       # Korzeń
        get_preorder(node.left, result)  # Lewo
        get_preorder(node.right, result) # Prawo
    return result

def get_inorder( node, result):
    if node:
        get_inorder(node.left, result)   # Lewo
        result.append(str(node.key))        # Korzeń
        get_inorder(node.right, result)  # Prawo
    return result

def get_postorder(node, result):
    if node:
        get_postorder(node.left, result)  # Lewo
        get_postorder(node.right, result) # Prawo
        result.append(str(node.key))         # Korzeń
    return result