#tutaj sie znajduje menu naszego programu
import sys
from tree import BST, AVL
#funkcja wyswitlajaca pomoc
def show_help():
    print("Help         Show this message")
    print("Print        Print the tree usin In-order, Pre-order, Post-order")
    print("Remove       Remove elements of the tree")
    print("Delete       Delete the whole tree")
    print("Export       Export tree to tikzpicture")
    print("Rebalance    Rebalance tree")
    print("Exit         Exit the program(same as Ctrl+D)")
#glowna fukcja
def main():
    tree_type = "BST"
    if "--tree" in sys.argv:
        idx = sys.argv.index("--tree")
        if idx + 1 < len(sys.argv):
            tree_type = sys.argv[idx + 1]

    # Tworzymy odpowiedni obiekt
    tree = AVL() if tree_type == "AVL" else BST()

    try:
        
        try:
            nodes_count = input("nodes> ").strip()
            if not nodes_count: return
            
            vals_raw = input("insert> ").strip()
            elements = [int(x) for x in vals_raw.split()]
            
            if tree_type == "AVL":
                tree.build_from_sorted(elements)
                print(f"Sorted: {sorted(elements)}")
                print(f"Median: {sorted(elements)[len(sorted(elements)) // 2]}")
            else:
                print(f"Inserting: {', '.join(map(str, elements))}")
                for val in elements:
                    tree.insert(val)
        except EOFError:
            return
    
        while True:
        
            try:
                command =input("action> ").strip()
            except EOFError:
                break
            if command == "Help":
                show_help()
            elif command == "Print":
                print("----Wypisywanie drzewa w trzech postaciach----")
                #tu jeszcze nie zrobilismy(wyswietla pre, in, post -order)
            elif command == "Remove":
                print("----Usuwanie elementu/ow drzewa----")
                #func to delete tree
            elif command == "Delete":
                print("----Usuwanie calkowite drzewa----")
                #func to delete whole tree
            elif command == "Export":
                print("----Eksport drzewa do tikzpicture----")
                #func to export tree to tikzpicture
            elif command == "Rebalance":
                print("----Przestawianie drzewa----")
                #func to rebalance tree
            elif command == "Exit":
                break
            else:
                print(f"Unknown command: {command}")
    except (KeyboardInterrupt, EOFError):
            pass
    except ValueError:
            sys.exit(1)
    print("Programm exited with status 0")
if __name__ == "__main__":
    main()
        