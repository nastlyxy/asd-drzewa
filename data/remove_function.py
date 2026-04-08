def handle_remove(tree):
    if tree.root is None:
        print("Tree is empty")
        return

    try:
        nodes_str = input("nodes> ").strip()
        if not nodes_str:
            return
        nodes_count = int(nodes_str)
    
        val_str = input("delete> ").strip()
        if not val_str:
            return
        
        elements = [int(x) for x in val_str.split()]
        
        elements = elements[:nodes_count]
        
        for val in elements:
            if tree.search(val):
                tree.remove(val)
                print(f"Value {val} was removed from the tree.")
            else:
                print(f"Value {val} is not in the tree.")
                
    except ValueError:
        print("Invalid input. Please enter numbers.")
    except EOFError:
        pass