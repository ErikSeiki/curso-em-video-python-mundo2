sexo = str(input("Digite o seu sexo entre o M ou F: ").upper().strip()[0])
while sexo != "M" and sexo != "F":
    sexo = str(input("Não a essa opção de escolha, digite novamente; ").upper().strip()[0])
if sexo == "M":
    print("Então voce é homem!")
else:
    print("Então voce é mulher!")
print("=-"*20)
sexo = str(input("Digite o seu sexo entre o M ou F: ").upper().strip()[0])
while sexo not in "MmFf":
    sexo = str(input("Dados invalidos, porfavor informe seu sexo; ").upper().strip()[0])
print("Sexo {} registrado com sucesso.".format(sexo))
