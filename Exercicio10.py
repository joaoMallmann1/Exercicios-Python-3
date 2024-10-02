"""
Peça ao usuário um número e use um loop para imprimir esse número elevado ao quadrado de 1 até 10.
"""
num = int(input("Digite um valor: "))

for n in range(1, 11):
    resultado = num ** n
    print(resultado)
