def clean_tree_recursive(node):
    if node is None:
        return
    clean_tree_recursive(node.left)
    clean_tree_recursive(node.right)
    node.left = None
    node.right = None
    return None