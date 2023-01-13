# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual o valor do produto? R$'))
desconto = preço - (preço * 5 / 100)
print(f'O preço original do produto é R${preço} e com 5% de desconto fica R${desconto}')