from math import radians, cos, sin, tan
angulo = float(input("Digite o angulo desejado: "))
seno = sin(radians(angulo))
print("O angulo de {} tem o SENO de {:.2f}".format(angulo, seno))
cosseno = cos(radians(angulo))
print("O angulo de {} tem o COSSENO de {:.2f}".format(angulo, cosseno))
tangente = tan(radians(angulo))
print("O angulo de {} tem a TANGENTE de {:.2f}".format(angulo, tangente))

#Programa que apresenta o Seno, Cosseno e a Tangente de um ângulo.