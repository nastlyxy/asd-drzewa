#tutaj sie znajduje menu naszego programu
import sys
import time
from tree import BST, AVL
from print_functions import  get_preorder, get_inorder, get_postorder, export_tikz
from delete_function import clean_tree_recursive
from remove_function import handle_remove

#Displays the list of available commands to the user.
def show_help():
    print("Help         Show this message")
    print("MinMax       Find minimum and maximum element")
    print("Print        Print the tree usin In-order, Pre-order, Post-order")
    print("Remove       Remove elements of the tree")
    print("Delete       Delete the whole tree")
    print("Export       Export tree to tikzpicture")
    print("Rebalance    Rebalance tree")
    print("Exit         Exit the program(same as Ctrl+D)")


    """
    Main application loop. Handles terminal arguments, tree initialization,
    and routes user commands to the corresponding logic.
    """
def main():

    # Default tree is BST unless overridden via terminal arguments
    tree_type = "BST"
    if "--tree" in sys.argv:
        idx = sys.argv.index("--tree")
        if idx + 1 < len(sys.argv):
            tree_type = sys.argv[idx + 1]
    tree = AVL() if tree_type == "AVL" else BST()

    try:

        #INITIALIZATION BLOCK
        
        try:
            nodes_count_str = input("nodes> ").strip()
            if not nodes_count_str: return
            nodes_count = int(nodes_count_str)

            # Strict loop: forces user to input the exact amount of numbers promised
            while True:
                vals_raw = input("insert> ").strip()
                elements = [int(x) for x in vals_raw.split()]
                
                if len(elements) != nodes_count:
                    print(f"Uwaga: Wprowadzono {len(elements)} liczb. Oczekiwano {nodes_count}. Sprobuj ponownie.")
                    continue
                else:
                    break
            
            if tree_type == "AVL":
                sorted_elements = sorted(elements)
                print(f"Sorted: {', '.join(map(str, sorted_elements))}")
                if sorted_elements:
                    median_idx = len(sorted_elements) // 2
                    print(f"Median: {sorted_elements[median_idx]}")
                
                tree.build_from_sorted(sorted_elements)
            else:
                print(f"Inserting: {', '.join(map(str, elements))}")
                for val in elements:
                    tree.insert(val)
        except EOFError:
            # Handles EOF during initialization (e.g., empty file redirection)
            return
        
        #MAIN ACTION LOOP
        while True:
        
            try:
                command =input("action> ").strip()
            except EOFError:
                break

            # Command Routing
            if command == "Help":
                show_help()
            elif command == "Print":
                if tree.root is None:
                    print("Tree is empty")
                else:
                    print("----Wypisywanie drzewa w trzech postaciach----")
                    #tu jeszcze nie zrobilismy(wyswietla pre, in, post -order)
                    print(f"Pre-order:  {', '.join(get_preorder(tree.root, []))}")
                    print(f"In-order:   {', '.join(get_inorder(tree.root, []))}")
                    print(f"Post-order: {', '.join(get_postorder(tree.root, []))}")
            elif command == "MinMax":
                if tree.root is None:
                    print("Tree is empty")
                else:
                    print("----Wyszukiwanie min/max----")
                    print(f"Min: {tree.find_min()}")
                    print(f"Max: {tree.find_max()}")        
            elif command == "Remove":
                print("----Usuwanie elementu/ow drzewa----")
                #func to delete tree
                handle_remove(tree)
            elif command == "Delete":
                print("----Usuwanie calkowite drzewa----")
                #func to delete whole tree
                if tree.root is None:
                    print("Tree is empty")
                else:
                    deleted_nodes = []
                    clean_tree_recursive(tree.root, deleted_nodes)

                    print(f"Deleting: {' '.join(deleted_nodes)}")
                    print("Tree successfully removed")
                    tree.root = None
    
            elif command == "Export":
                print("----Eksport drzewa do tikzpicture----")
                if tree.root is None:
                    print("Tree is empty")
                else:
                    # Wraps the recursive TikZ nodes in the LaTeX boilerplate
                    tikz_nodes = f"\\{export_tikz(tree.root)};"
                    full_tikz = f"""\\begin{{tikzpicture}}[
        level distance=1.5cm,
        level 1/.style={{sibling distance=4cm}},
        level 2/.style={{sibling distance=2cm}},
        level 3/.style={{sibling distance=1cm}},
        every node/.style = {{shape=circle, draw=green, fill=red!30, thick, minimum size=8mm, inner sep=1pt}}
    ]
    {tikz_nodes}
\\end{{tikzpicture}}"""
                   
                    print(full_tikz)

                    # Automatically write the LaTeX code to a file
                    with open("drzewo_export.tex", "w", encoding="utf-8") as f:
                        f.write(full_tikz)
                        
                    print("\nKod zostal zapisany do pliku: drzewo_export.tex")
            elif command == "Rebalance":
                print("----Przestawianie drzewa----")
                if tree_type == "BST":
                    tree.rebalance()
                    pre_order_result = get_preorder(tree.root, [])
                    
                    print(f"Pre-Order: {', '.join(pre_order_result)}")
                else:
                    print("AVL tree is automatically balanced. No action needed.")
            elif command == "Exit":
                break
            else:
                print(f"Unknown command: {command}")
    # Gracefully handle Ctrl+C or Ctrl+D user interruptions            
    except (KeyboardInterrupt, EOFError):
            pass
    # Catch conversion errors (e.g., trying to parse letters into ints)
    except ValueError:
            sys.exit(1)
    print("Programm exited with status 0")
if __name__ == "__main__":
    main()
        