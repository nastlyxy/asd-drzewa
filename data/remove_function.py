def handle_remove(tree):
    if tree.root is None:
        print("Tree is empty")
        return
    try:
        val_str = input("value/s to remove> ").strip()
        
        if not val_str:
            return
        
        elements = [int(x) for x in val_str.split()]
       
        for val in elements:
            if tree.search(val):
                tree.remove(val)
                print(f"Value {val} was removed from the tree.")
            else:
                print(f"Value {val} is not in the tree.")
        
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
    except EOFError:
        pass