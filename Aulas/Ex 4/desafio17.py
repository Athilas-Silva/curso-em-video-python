from math import hypot
co = float(input("Comprimento do Cateto Oposto: "))
ca = float(input("Comprimento do Cateto Adjacente: "))
hi = hypot(co, ca)
print("A hipotenusa vai ser de {:.2f}".format(hi))

#Outra forma para executar com matematica

# co = float(input("Informe o Comprimento do Cateto Oposto: "))
# ca = float(input("Informe o Comprimento do Cateto Adjacente: "))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print("A hipotenusa vai ser de {:.2f}".format(hi))

#Programa que a presenta a hipotenusa de um triangulo