"""
Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000, imprimindo seu valor na
tela, até que seu valor seja 100000
"""
int = 0
for numero in range(0, 100001, 1000):
    print(numero)

while int < 100000:
    print(int)
    int += 1000
