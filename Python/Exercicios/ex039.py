from datetime import date

print('Faça um programa que leia o ano de nascimento de uma jovem e informe,\n'
      'de acordo com sua idade, se ele ainda vai se alistar ao serviço militar\n'
      'se é a hora de se alistar ou seja ja passou do tempo do alistamento.\n'
      'Seu programa tambem deverá msotrar o tempo que falta ou que passou do prazo\n')

print(30*'-=-')
print('\n')

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = idade - 18
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = 18 - idade
    print('Você ja deveria ter se alistado a {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
    
