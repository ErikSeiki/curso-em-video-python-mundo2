'''
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
'''

frase= input("Digite uma frase: ").strip()
palavra = frase.upper()
palavra = palavra.split()
junto = "".join(palavra)
tamanho = len(junto)
inverso = ""
for letra in range(tamanho-1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print('Essa frase "{}" é uma palindromo'.format(frase.capitalize()))
else:
    print('Essa frase "{}" não é uma palindromo'.format(frase.capitalize()))

print("-="* 20)

f = input("Digite uma frase: ").strip()
p = f.upper()
p = p.split()
j = "".join(p)
i = j[::-1]
print("O inverso de {} é {}".format(j, i))
if i == j:
    print('Essa frase "{}" é uma palindromo'.format(f.capitalize()))
else:
    print('Essa frase "{}" não é uma palindromo'.format(f.capitalize()))