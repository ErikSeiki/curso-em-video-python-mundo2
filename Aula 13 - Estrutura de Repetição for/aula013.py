'''
for c in range(1, 6):
    print(c)
print("=-" * 20)

n = int(input("Digite um numero: "))
for c in range(0, n + 1):
    print(c)
print("=-" * 20)

i = int(input("Digite o inicio: "))
f = int(input("Digite o fim: "))
p = int(input("Digite o passo: "))
for c in range(i, f + 1, p):
    print(c)
print("=-"*20)
'''
s = 0
for c in range(0,3):
   n = int(input("Digite um valor: "))
   s = s +n
print('Somatorio de todoso os numeros foi de {}'.format(s))
