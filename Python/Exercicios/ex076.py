t = ("Lapis", 1.75,
    "Borracha", 2.00,
    "Caderno", 15.00,
    "Transferidor", 25.00,
    "Compasso", 4.20,
    "Mochila", 9.99,
    "Canetas", 22.30,
    "Livro", 34.90)
print("="*37)
print("LISTAGEM DE PREÇOS")
print("="*37)
for item in range(0, len(t)):
    if item % 2 == 0:
        print(f"{t[item]:.<30}", end="")
    else:
        print(f"{t[item]:>5.2f}")
