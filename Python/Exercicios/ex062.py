primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:    
    total = total + mais
    while cont <= total:
        print(f"{termo} ", end="")
        termo = termo + razao
        cont = cont + 1
    print("PAUSE")
    mais = int(input("Quantos termos voce quer mostrar a mais? "))
print(f"Progressao finalizada com {total} termos mostrados")
