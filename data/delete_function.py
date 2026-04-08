def clean_tree_recursive(node, deleted_nodes):
    if node is None:
        return
    clean_tree_recursive(node.left, deleted_nodes)
    clean_tree_recursive(node.right, deleted_nodes)
    deleted_nodes.append(str(node.key))

    node.left = None
    node.right = None