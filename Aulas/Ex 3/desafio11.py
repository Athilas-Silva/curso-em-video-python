lar = float(input("Informe a largura da parede: "))
alt = float(input("Informe a altura da parede: "))
area = lar * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(lar, alt, area))
tinta = area / 2
print('Para pintar essa parede você precisará de {}L de tinta'.format(tinta))

#Programa que mostra a quantidade de litros que um pintor precisará para pintar uma parede