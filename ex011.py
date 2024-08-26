l = float(input('Digite a largura da sua parede: '))
a = float(input('Digite a altura da sua parede: '))
print('Sua parede tem a dimensão de {}x{} e a sua área é de {}m²'.format(l, a, (l*a) ))
print('Para pintar essa parede serão necessários {}l'.format(((l*a)/2)))