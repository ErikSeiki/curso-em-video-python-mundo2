a = float(input("Digite o tamanho da primeira reta: "))
b = float(input("Digite o tamanho da segunda reta: "))
c = float(input("Digite o tamanho da terceira reta: "))

if a < b + c and b < a + c and c < a + b:
    print("É possivel ser um triagulo")
    if a == b == c:
        print("Triangulo equilatero")
    elif a != b != c != a:
        print("Triangulo escaleno")
    else:
        print("Triangulo isosceles")
else:
    print("Não é possivel ser um triangulo")
