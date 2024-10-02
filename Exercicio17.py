"""
Dada uma lista de números, use um loop para somar apenas os números pares.
"""
lista = []
sequencia = '1'
pares = 0

while sequencia.lower() != 'fim':
    sequencia = input("Digite uma lista de números para somar os seus valores pares (Digitar fim para parar): ")
    if sequencia.isdigit():
        lista.append(sequencia)

for i in lista:
    if int(i) % 2 == 0:
        pares += int(i)

print(pares)
