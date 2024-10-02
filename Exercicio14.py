"""
Imprima os primeiros 10 números da sequência de Fibonacci.
"""
a = 0
b = 1

print(b)

for _ in range(9):
    proximo = a + b
    print(proximo)
    a = b
    b = proximo



