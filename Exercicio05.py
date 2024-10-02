"""
Peça ao usuário um número e imprima a tabuada desse número até 10.
"""
num = float(input("Digite um número para mostrar sua tabuada: "))

for n in range(1, 11):
    print(f"{num} * {n} = {num * n:.2f}")