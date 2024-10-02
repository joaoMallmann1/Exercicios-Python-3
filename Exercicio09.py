"""
Peça ao usuário uma sequência de números (até que ele insira 0) e conte quantos números negativos foram
inseridos.
"""
sequencia = 1
numeros = []
negativos = 0

while sequencia != 0:
    sequencia = int(input("Digite uma sequência de números, e, quando quiser parar, digitar 0 para contar"
                          " os negativos: "))

    numeros.append(sequencia)

    if sequencia == 0:
        break


for numero in numeros:
    if numero < 0:
        negativos += 1

print(f"Foram inserido {negativos} números negativos.")
