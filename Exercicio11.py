"""
Peça ao usuário um número inteiro e calcule a soma de seus dígitos.
"""
num = input("Digite um valor para somar seus algarismos: ")
soma = 0

if num.isdigit():
    for i in num:
        soma += int(i)

print(soma)
