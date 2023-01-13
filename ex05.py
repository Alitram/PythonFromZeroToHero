# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

NotaPortuguês = float(input('Português: '))
NotaMatemática = float(input('Matemática: '))
NotaFinal = (NotaPortuguês + NotaMatemática) / 2
print(f'A média do aluno é de {NotaFinal:.1f}')