real = float(input('Quanto dinheiro voc� tem na carteira? R$ '))
dolar = real / 3.27
print('Com R${:.2F} voc� pode comprar US$ {:.2f}'.format(real, dolar))