# calcular a area de uma parede e a quantidade de tinta necessaria para pinta-la 1Ltinta == 2m²parede 
n1 = float(input('infome a largura da parede em metros: '))
n2 = float(input('infome a altura da parede em metros: '))
area = n1 * n2 
tinta = area / 2 
print('para pintar uma parede de {}m² e necessario {}L de tinta'.format(area, tinta))
