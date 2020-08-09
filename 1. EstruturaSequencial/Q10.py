'''
Questao 10
Faça um Programa que peca a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
'''

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 1.8 + 32
print("{:.0f}º Celsius == {:.1f}º Fahrenheit.".format(celsius, fahrenheit))

'''
Formula de conversao: T(°C) = (T(°F) - 32) × 5/9
https://www.rapidtables.com/convert/temperature/fahrenheit-to-celsius.html

{:...} -> Format Specification Mini-Language
https://docs.python.org/3/library/string.html#format-specification-mini-language
'''
