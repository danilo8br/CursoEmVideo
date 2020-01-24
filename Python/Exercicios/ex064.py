# Minha solução
soma = 0
cont = 0
n = 0
while n != 999:
    n = int(input("Digite um numero para [999 para parar]: "))
    if n != 999:
        cont = cont + 1
        soma = soma + n
print(f"Voce digitou {cont} numeros e a soma entre eles foi {soma}")


# Solução do guanabara

num = cont = soma = 0
num = int(input("Digite um numero para [999 para parar]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um numero [999 para parar]: "))
print(f"Voce digitou {cont} numeros e a soma entre eles foi {soma}")
