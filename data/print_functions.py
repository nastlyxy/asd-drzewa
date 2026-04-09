#tutaj będa funkcje dla komendy print
from tree import BST, AVL
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#TREE TRAVERSAL ALGORITHMS
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


#EXPORT FEATURE
def export_tikz(node):
    if node is None:
        return ""
        
    if node.left is None and node.right is None:
        return f"node {{{node.key}}}"
        
    l_str = f"child {{ {export_tikz(node.left)} }}" if node.left else "child[missing] {}"
    r_str = f"child {{ {export_tikz(node.right)} }}" if node.right else "child[missing] {}"
    
    return f"node {{{node.key}}}\n{l_str}\n{r_str}"