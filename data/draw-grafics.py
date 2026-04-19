import json
import matplotlib.pyplot as plt
import os

def draw_plots():
    if not os.path.exists('wyniki.json'):
        print("Błąd: Nie znaleziono pliku 'wyniki.json'. Najpierw uruchom main.py!")
        return

    # Wczytanie danych z pliku
    with open('wyniki.json', 'r') as f:
        data = json.load(f)

    sizes = data['sizes']

    # Konfiguracja głównego okna (siatka 2x2)
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Empiryczna analiza złożoności czasowej drzew BST i AVL', fontsize=16, fontweight='bold')

    # Styl linii: zdegenerowane BST to czerwona przerywana, zbalansowane AVL to niebieska ciągła
    bst_style = 'r--'
    avl_style = 'b-'

    # [0, 0] Tworzenie struktury
    axs[0, 0].plot(sizes, data['bst_create'], bst_style, label='BST (niezbalansowane)', linewidth=2)
    axs[0, 0].plot(sizes, data['avl_create'], avl_style, label='AVL', linewidth=2)
    axs[0, 0].set_title('Tworzenie struktury t=f(n)')
    axs[0, 0].set_xlabel('Liczba elementów n')
    axs[0, 0].set_ylabel('Czas [s]')
    axs[0, 0].legend()
    axs[0, 0].grid(True, linestyle=':', alpha=0.7)

    # [0, 1] Szukanie Min/Max
    axs[0, 1].plot(sizes, data['bst_minmax'], bst_style, label='BST (niezbalansowane)', linewidth=2)
    axs[0, 1].plot(sizes, data['avl_minmax'], avl_style, label='AVL', linewidth=2)
    axs[0, 1].set_title('Wyszukiwanie min/max t=f(n)')
    axs[0, 1].set_xlabel('Liczba elementów n')
    axs[0, 1].set_ylabel('Czas [s]')
    axs[0, 1].legend()
    axs[0, 1].grid(True, linestyle=':', alpha=0.7)

    # [1, 0] Wypisywanie in-order
    axs[1, 0].plot(sizes, data['bst_inorder'], bst_style, label='BST (niezbalansowane)', linewidth=2)
    axs[1, 0].plot(sizes, data['avl_inorder'], avl_style, label='AVL', linewidth=2)
    axs[1, 0].set_title('Wypisywanie in-order t=f(n)')
    axs[1, 0].set_xlabel('Liczba elementów n')
    axs[1, 0].set_ylabel('Czas [s]')
    axs[1, 0].legend()
    axs[1, 0].grid(True, linestyle=':', alpha=0.7)

    # [1, 1] Równoważenie drzewa (tylko BST)
    axs[1, 1].plot(sizes, data['bst_balance'], 'g-.', label='Równoważenie DSW', linewidth=2)
    axs[1, 1].set_title('Równoważenie zdegenerowanego BST t=f(n)')
    axs[1, 1].set_xlabel('Liczba elementów n')
    axs[1, 1].set_ylabel('Czas [s]')
    axs[1, 1].legend()
    axs[1, 1].grid(True, linestyle=':', alpha=0.7)

    # Poprawia odstępy między wykresami, żeby napisy na siebie nie nachodziły
    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
    
    # Zapisuje obrazek do pliku
    plt.savefig('wykresy_wyniki.png', dpi=300) # dpi=300 daje super jakość do PDFa
    print("Sukces! Wykres zapisano jako 'wykresy_wyniki.png'. Możesz go dodać do sprawozdania.")

if __name__ == "__main__":
    draw_plots()