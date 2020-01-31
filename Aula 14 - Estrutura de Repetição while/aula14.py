'''
from time import sleep
x = 0
while not x == 15:
    x += 1
    print(x)
    sleep(0.5)
print("End")
print('=-'*20)
n = 1
while n != 0:
    n = int(input("Digite um valor: "))
print("Fim")
print('=-'*20)
from time import sleep
x = 0
n = 50
while x != n:
    print(x)
    x += 1
    if x % 2 == 0:
        n += 1
    sleep(0.3)
print("Valor de x = {} valor de n = {}".format(x,n))
print('=-'*20)
'''
a = 1
par = impar = 0
while a != 0:
    a = int(input("Digite um valor: "))
    if a != 0:
        if a % 2 == 0:
            par += 1
        else:
            impar += 1
print("Voce digitou {} numeros pares e {} numeros impares!".format(par, impar))
