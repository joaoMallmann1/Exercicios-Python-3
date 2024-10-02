"""
Peça ao usuário uma string e conte quantas vogais existem nela.
"""
data = input("Digite uma palavra para contar suas vogais: ")
vogais = 0

for i in data:
    if i in ['a', 'e', 'i', 'o', 'u']:
        vogais += 1

print(f"A palavra {data} tem {vogais} vogais ")
