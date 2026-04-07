def handle_remove(tree):
    if tree.root is None:
        print("Tree is empty")
        return
    try:
        val_str = input("value to remove> ").strip()
        
        if not val_str:
            return
        
        val = int(val_str)
        
        tree.remove(val)
        print(f"Value {val} was removed from the tree.")
        
    except ValueError:
        print("Invalid input. Please enter a number.")
    except EOFError:
        pass