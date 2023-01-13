#  Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual o salário do funcionário? R$'))
quinze = sal + (sal * 15 / 100)
print(f'Um funcionário que ganhava R${sal}, com 15% de aumento, passa a receber R${quinze:.2f}')