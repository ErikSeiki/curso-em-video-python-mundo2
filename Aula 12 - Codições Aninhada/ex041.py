import datetime

nasc = int(input("Digite o ano em que voce nasceu: "))
atu = datetime.date.today().year
a = atu - nasc
if a <= 9:
    print("Mirim")
elif a > 9 and a <= 14:
    print("Infantil")
elif a > 14 and a <= 19:
    print("Junior")
elif a > 19 and a <= 25:
    print("Sênior")
else:
    print("Master")
