maior = homens = mulher = 0
while True:
    idade = int(input("Idade: "))

    sexo = " "
    while sexo not in "MmFf":
        sexo = str(input("Sexo: "))
    if idade > 18:
        maior += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulher += 1
        
    continuar = " "    
    while continuar not in "SsNn"    
        continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break
print(f"Total de pessoas maiores de 18 anos: {maior}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mulher} com menos de 20 anos")
