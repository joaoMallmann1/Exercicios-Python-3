"""
Crie um programa que verifique se um número é primo.
"""
numero = int(input("Digite um número para verificar se este é primo: "))

if numero > 1:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"O número {numero} não é primo")
            break
    else:
        print(f"O número {numero} é primo")
if numero == 0:
    print("O número é zero")
elif numero < 0:
    print("O número é negativo")
