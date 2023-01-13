# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# De tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a aultura da parede: '))
área = largura * altura

print(f'A sua parede tem a dimensão de {largura}x{altura} e sua área é de {área}m²')
print(f'Para pintar essa parede você precisa de {área / 2}l de tinta')