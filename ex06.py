# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Distância em metros: '))
print(f"""A medida de {metros}m corresponde a
{metros / 1000}km
{metros / 100}hm
{metros / 10}dam
{metros / 0.10000:.0f}dm
{metros * 100:.0f}cm
{metros * 1000:.0f}mn""")