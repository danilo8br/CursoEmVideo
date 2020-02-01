total = totmil = cont = menor = 0
barato = " "
while True:
    nome = str(input("Nome do produto: "))
    preco = float(input("Preço: "))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
        
    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input("Quer continuar? [S/N]"))
    if continuar == "N":
        break
print(f"O total da compra foi de {total}")
print(f"Temos {totmil} produtos custando mais de R$1000")
print(f"O produto mais barato foi {barato} que custa R${menor}")
