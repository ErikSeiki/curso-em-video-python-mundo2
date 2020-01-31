i = int(input("Digite o primeiro termo: "))
r = int(input("Digite razao: "))
print(i, end=" → ")
for c in range(0, 9):
    i = i + r
    print(i, end=" → ")
print("END")

p = int(input("Digite o primero termo: "))
ra = int(input("Digite a razão: "))
d = p + (10 - 1) * ra
for a in range(p, d + 1, ra):
    print('{} '.format(a), end="→ ")
print("END")
