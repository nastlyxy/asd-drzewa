#Handles the interactive process of removing multiple elements from the tree. Includes strict validation to ensure the user provides the exact number of elements.
def handle_remove(tree):
    if tree.root is None:
        print("Tree is empty")
        return

    try:
        nodes_str = input("nodes> ").strip()
        if not nodes_str:
            return
        nodes_count = int(nodes_str)
    
        while True:
            val_str = input("delete> ").strip()
            if not val_str:
                return
                
            elements = [int(x) for x in val_str.split()]
            
            if len(elements) != nodes_count:
                print(f"Uwaga: Wprowadzono {len(elements)} liczb. Oczekiwano {nodes_count}. Sprobuj ponownie.")
                continue
            else:
                break
        
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