#tutaj będa funkcje dla komendy print
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def get_preorder(self, node, result):
    if node:
        result.append(str(node.key))       # Korzeń
        self.get_preorder(node.left, result)  # Lewo
        self.get_preorder(node.right, result) # Prawo
    return result

def get_inorder(self, node, result):
    if node:
        self.get_inorder(node.left, result)   # Lewo
        result.append(str(node.key))        # Korzeń
        self.get_inorder(node.right, result)  # Prawo
    return result

def get_postorder(self, node, result):
    if node:
        self.get_postorder(node.left, result)  # Lewo
        self.get_postorder(node.right, result) # Prawo
        result.append(str(node.key))         # Korzeń
    return result