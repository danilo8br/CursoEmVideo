n = int(input('Digite um número: '))
a = n * 2
b = n * 3
c = n ** (1/2)

print('O dobro de {} vale {}.'.format(n, a))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:2f}.'.format(n, b, n, c))

#Também da pra utilizar as variaveis dentro do format.
