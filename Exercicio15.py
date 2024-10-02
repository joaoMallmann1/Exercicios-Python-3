"""
Peça ao usuário uma string e use um loop para invertê-la.
"""
data = input("Digite uma palavra para invertê-la: ")
inversao = ''

for i in range(len(data) - 1, -1, -1):
    inversao += data[i]

print(inversao)
