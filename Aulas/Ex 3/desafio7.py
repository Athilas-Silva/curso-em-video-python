n1 = int(input("Informe a primeira nota: "))
n2 = int(input("Informe a segunda nota: "))
n3 = int(input("Informe a terceira nota: "))
n4 = int(input("Informe a quarta nota: "))
md = (n1 + n2 + n3 + n4) / 4
# ou md = (n1 + n2 + n3 + n4) // 4
print("A média do aluno é {}".format(md))

# / Calculo usado para ter número real ( números quebrados, ou seja, com virgula)
# // Calculo usado para ter o número inteiro da divisão, sem virgula
# Programa para medir a média de um aluno com divisão inteira e de forma tradicional