import json
import matplotlib.pyplot as plt

# Wczytanie danych z pliku
with open('wyniki.json', 'r') as f:
    data = json.load(f)

sizes = data['sizes']

# Ustawienia ogólne stylu
plt.style.use('seaborn-v0_8-whitegrid')

# ---------------------------------------------------------
# Wykres 1: Tworzenie struktury
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.plot(sizes, data['bst_create'], label='BST', color='#e74c3c', linestyle='--', linewidth=2)
plt.plot(sizes, data['avl_create'], label='AVL', color='#3498db', linestyle='-', linewidth=2)
plt.title('Tworzenie struktury (drzewo zdegenerowane)', fontsize=14)
plt.xlabel('Liczba elementów (n)', fontsize=12)
plt.ylabel('Czas (s) - skala logarytmiczna', fontsize=12)
plt.yscale('log')
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('wykres_1_tworzenie.png', format='png')
plt.close()

# ---------------------------------------------------------
# Wykres 2: Wyszukiwanie Min/Max
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.plot(sizes, data['bst_minmax'], label='BST', color='#e74c3c', linestyle='--', linewidth=2)
plt.plot(sizes, data['avl_minmax'], label='AVL', color='#3498db', linestyle='-', linewidth=2)
plt.title('Wyszukiwanie Min/Max', fontsize=14)
plt.xlabel('Liczba elementów (n)', fontsize=12)
plt.ylabel('Czas (s) - skala logarytmiczna', fontsize=12)
plt.yscale('log')
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('wykres_2_minmax.png', format='png')
plt.close()

# ---------------------------------------------------------
# Wykres 3: Wypisywanie In-Order
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.plot(sizes, data['bst_inorder'], label='BST', color='#e74c3c', linestyle='--', linewidth=2)
plt.plot(sizes, data['avl_inorder'], label='AVL', color='#3498db', linestyle='-', linewidth=2)
plt.title('Wypisywanie In-Order', fontsize=14)
plt.xlabel('Liczba elementów (n)', fontsize=12)
plt.ylabel('Czas (s) - skala logarytmiczna', fontsize=12)
plt.yscale('log')
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('wykres_3_inorder.png', format='png')
plt.close()

# ---------------------------------------------------------
# Wykres 4: Równoważenie drzewa BST (DSW)
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.plot(sizes, data['bst_balance'], label='BST (DSW)', color='#2ecc71', linestyle='-', linewidth=2)
plt.title('Równoważenie drzewa BST (algorytm DSW)', fontsize=14)
plt.xlabel('Liczba elementów (n)', fontsize=12)
plt.ylabel('Czas (s)', fontsize=12)
# Tu nie dajemy skali logarytmicznej, bo mamy tylko jedną linię liniową
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('wykres_4_dsw.png', format='png')
plt.close()

print("Wygenerowano 4 osobne pliki PDF z wykresami.")