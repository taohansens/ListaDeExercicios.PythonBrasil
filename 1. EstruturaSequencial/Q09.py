'''
Questao 09
Faca um Programa que peca a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
'''

fahrenheit = float(input("Digite a temperatura em Farenheit: "))
celsius = (fahrenheit-32)/1.8
print("{:.0f}º Fahrenheit == {:.2f}º Celsius.".format(fahrenheit, celsius))

'''
Formula de conversao: T(°C) = (T(°F) - 32) × 5/9
https://www.rapidtables.com/convert/temperature/fahrenheit-to-celsius.html

{:...} -> Format Specification Mini-Language
https://docs.python.org/3/library/string.html#format-specification-mini-language
'''
