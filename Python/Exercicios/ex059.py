from time import sleep

primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))
opcao = 0 
while opcao != 5:
    print(""" 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa
    """)
    opcao = int(input("Qual a sua opção: "))
    if opcao == 1:
        soma = primeiro + segundo
        print(f"A soma entre {primeiro} + {segundo} é igual a {soma}")
        sleep(0.5)
    elif opcao == 2:
        multiplicar = primeiro * segundo
        print(f"O resultado de {primeiro} x {segundo} é igual a {multiplicar}")
        sleep(0.5)
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print(f"Entre {primeiro} e {segundo} o maior é {maior}")
        sleep(0.5)
    elif opcao == 4:
        print("Digite os valores novamente: ")
        primeiro = int(input("Primeiro valor: "))
        segundo = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando o programa... ")
        sleep(1.0)
    else:
        print("Opcao invalida, tente novamente")
print("Fim do programa")
