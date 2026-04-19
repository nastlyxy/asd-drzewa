import time
import numpy as np
import json
from print_functions import get_inorder
from tree import BST, AVL 

def measure_average_time(func, *args, **kwargs):
    """Mierzy czas zegarowy 4 razy i zwraca średnią."""
    measurements = []
    for _ in range(4):
        start = time.perf_counter()
        func(*args, **kwargs)
        measurements.append(time.perf_counter() - start)
    return sum(measurements) / 4

def main():
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    
    results = {
        'sizes': sizes,
        'bst_create': [], 'avl_create': [],
        'bst_minmax': [], 'avl_minmax': [],
        'bst_inorder': [], 'avl_inorder': [],
        'bst_balance': []
    }

    for size in sizes:
        print(f"Pomiary dla n={size}...")
        
        filename = f'benchmark/increasing_array_{size:05d}.txt'
        data = np.loadtxt(filename, dtype=int)[1:].tolist() 

        # --- A/B. TWORZENIE ---
        def build_bst():
            temp_bst = BST()
            for key in data: temp_bst.insert(key)
            return temp_bst

        results['bst_create'].append(measure_average_time(build_bst))
        
        avl = AVL()
        results['avl_create'].append(measure_average_time(avl.build_from_sorted, data))
        
        bst = build_bst()

        # --- C. MIN/MAX ---
        def find_min_max_bst(): bst.find_min(); bst.find_max()
        def find_min_max_avl(): avl.find_min(); avl.find_max()

        results['bst_minmax'].append(measure_average_time(find_min_max_bst))
        results['avl_minmax'].append(measure_average_time(find_min_max_avl))

        # --- D. IN-ORDER ---
        results['bst_inorder'].append(measure_average_time(get_inorder, bst.root, []))
        results['avl_inorder'].append(measure_average_time(get_inorder, avl.root, []))

        # --- E. RÓWNOWAŻENIE (DSW) ---
        def measure_rebalance():
            times = []
            for _ in range(4):
                temp_bst = build_bst()
                start = time.perf_counter()
                temp_bst.rebalance()
                times.append(time.perf_counter() - start)
            return sum(times) / 4

        results['bst_balance'].append(measure_rebalance())

    print("\nPomiary zakończone. Zapisuję wyniki do pliku 'wyniki.json'...")
    
    # Zapis do JSON, aby nowy plik mógł to odczytać
    with open('wyniki.json', 'w') as f:
        json.dump(results, f, indent=4)
        
    print("Gotowe! Możesz teraz uruchomić skrypt do rysowania wykresów.")

if __name__ == "__main__":
    main()