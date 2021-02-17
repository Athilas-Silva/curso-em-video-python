import random
nome1 = str(input("Informe o 1º nome: "))
nome2 = str(input("Informe o 2º nome: "))
nome3 = str(input("Informe o 3º nome: "))
nome4 = str(input("Informe o 4º nome: "))
nome5 = str(input("Informe o 5º nome: "))
nome6 = str(input("Informe o 6º nome: "))
nome7 = str(input("Informe o 7º nome: "))
nome8 = str(input("Informe o 8º nome: "))
lista = [nome1, nome2, nome3, nome4, nome5, nome6, nome7, nome8]
random.shuffle(lista)
print("A ordem de apresentação será:")
print(lista)

#Programa que sorteia os alunos para apresentação.