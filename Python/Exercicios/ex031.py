distancia = float(input('Qual a distância da sua viagem?'))
print('Voce esta prestes a começar uma viajem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
