# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar.
# Com esse guião o valor do dolar sempre estará atualizado

import requests

cot = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
cot = cot.json()
cotdollar = cot['USDBRL']["bid"]
dolar = float(cotdollar)

real = float(input('Quanto de dinheiro que você tem na sua carteira? R$'))
comprar = real / dolar
print(f'Cotação atual do Dólar é de $1 dólar equivale a R${dolar:.2f}')
print(f'Por tanto com R${real} você pode comprar ${comprar:.2f}')
