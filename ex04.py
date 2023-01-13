# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt
número = int(input('Digite um número: '))
print(f"""O dobro de {número} é {número * 2}
O triplo de {número} é {número * 3}
A raiz quadrada de {número} é {int(sqrt(número))}""")
