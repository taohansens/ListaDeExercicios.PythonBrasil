'''
Questao 08
Faca um Programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mes.
Calcule e mostre o total do seu salario no referido mes.
'''

valorHora = float(input("Digite quanto voce ganha por hora de trabalho: R$"))
horasTrabalhadas = int(input("Quantas horas voce trabalhou no mes? "))
salario = valorHora * horasTrabalhadas
print("Seu salario nesse mes foi de R${:.2f}".format(salario))

'''
{:...} -> Format Specification Mini-Language
https://docs.python.org/3/library/string.html#format-specification-mini-language
'''
