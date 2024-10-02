"""
Peça ao usuário 5 números e calcule a média usando um loop.
"""
contador = 0
soma = 0

while contador < 5:
    numero = float(input(f"Entre com o {contador + 1}° número: "))
    contador += 1
    soma += numero

media = soma / 5
print(f"A média desses 5 valores é de {media}")

