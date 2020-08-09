'''
Questao 06
Faca um Programa que peca o raio de um circulo, calcule e mostre sua area.
'''

raio = float(input("Digite o raio em cm: "))
area = 3.1416*(raio*raio)
print("A area do circulo com raio {:.0f}cm eh de {:.2f}cm².".format(raio, area))

'''
Pi ~= 3.1416
Area do circulo = pi * Raio²

{:...} -> Format Specification Mini-Language
https://docs.python.org/3/library/string.html#format-specification-mini-language
'''
