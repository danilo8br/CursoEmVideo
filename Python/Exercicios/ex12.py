preço = float(input('Qual o preço do produto? R$ '))
novo = preço - (produto * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar {}'.format(preço, novo))
