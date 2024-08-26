from math import radians, sin, cos, tan

an = float(input('Digite o angulo que você deseja: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cos))
print('O ângulo de {} tem a tângente de {:.2f}'.format(an, tan))