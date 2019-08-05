salario = float(input('Qual e o salario do funcionáro? '))
aumento =  salario + (salario * 15 / 100)
print('Um funcionario ganhava {}R$, com 15% de aumento, passa a receber {:.2f}'.format(salario, aumento))
