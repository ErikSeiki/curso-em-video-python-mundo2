peso = float(input("Digite seu peso: (Kg) "))
altura = float(input("Digite sua altura: (m) "))
imc = peso / (altura ** 2)
print("Seu imc é {:.1f}".format(imc))
if imc < 18.5:
    print("Voce esta Abaixo do Peso")
elif imc >= 18.5 and imc < 25:
    print("Voce esta Peso ideal")
elif imc >= 25 and imc < 30:
    print("Voce esta Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Voce esta Obesidade")
else:
    print("Voce esta Obesidade mórbida")
