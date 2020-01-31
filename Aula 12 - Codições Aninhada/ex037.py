n = int(input("Digite um numero: "))
print("Escolha a base numerica para a conversão sendo que,\n 1 - binario \n 2 - ohctal \n 3 - hexadecimal ")
e = int(input("Sua escolha:"))
if e == 1:
    print("Sua escolha foi binario, e o numero {} em binario é {}".format(n, bin(n)[2:]))
elif e == 2:
    print("Sua escolha foi octal, e o numero {} em octal é {}".format(n, oct(n)[2:]))
elif e == 3:
    print("Sua escolha foi hexadecimal, e o numero {} em hexadecimal é {}".format(n, hex(n)[2:]))
else:
    print("não a essa opção!")
