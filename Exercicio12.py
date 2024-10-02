"""
Peça ao usuário um número e calcule seu fatorial usando um loop for.
"""
indice = 1
num = int(input("Digite um número para checar seu fatorial: "))
resultado = 1

for i in range(1, num + 1):
    resultado *= i

print(resultado)
