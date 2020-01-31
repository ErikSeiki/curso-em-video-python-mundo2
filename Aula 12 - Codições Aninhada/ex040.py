n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print("1º nota: {:.1f}".format(n1))
print("2º nota: {:.1f}".format(n2))
print("Media: {:.1f}".format(m))
if m < 5:
    print("Aluno Reprovado")
elif m >= 5 and m < 7:
    print("Aluno Recuperação")
else:
    print("Aluno Aprovado")
