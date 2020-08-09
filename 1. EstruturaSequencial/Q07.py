'''
Questao 07
Faca um Programa que calcule a area de um quadrado, em seguida mostre o dobro desta area para o usuario.
'''

lado = float(input("Digite lado do quadrado: "))
areaDobro = (lado * lado)*2
print("O dobro da area do quadrado eh {:.0f}".format(areaDobro))

'''
Area do quadrado = base * altura  == lado²

{:...} -> Format Specification Mini-Language
https://docs.python.org/3/library/string.html#format-specification-mini-language
'''
