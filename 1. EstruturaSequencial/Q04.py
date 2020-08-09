'''
Questao 04
Faca um Programa que peca as 4 notas bimestrais e mostre a media.
'''

bim1 = float(input("Digite as nota do primeiro bimestre: "))
bim2 = float(input("Digite as nota do segundo bimestre: "))
bim3 = float(input("Digite as nota do terceiro bimestre: "))
bim4 = float(input("Digite as nota do quarto bimestre: "))
media = (bim1 + bim2 + bim3 + bim4) / 4
print("A media das notas eh {:.2f}".format(media))

'''

{:.2f} > Duas casas decimais, ponto flutuante
Format Specification Mini-Language
https://docs.python.org/3/library/string.html#format-specification-mini-language

Numeric Types — int, float, complex
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
'''
