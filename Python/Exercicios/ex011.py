larg = float(input('Digite a largura da sua parede: '))
alt = float(input('Digite a altura da sua parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
