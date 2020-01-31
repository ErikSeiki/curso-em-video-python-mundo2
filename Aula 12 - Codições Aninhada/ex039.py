import datetime

a = int(input("Digite o ano em que voce nasceu: "))
at = datetime.date.today().year
if (a + 18) < at:
    print(
        "Ja se passou o ano de alistamento. Voce devia ter se alistado ou voce se alistou a {} anos atras. O ano de {} ".format(
            at - (a + 18), a + 18))

elif (a + 18) > at:
    print("Ainda não chegou a ano de seu alistamento. Falta {} anos, para o ano {}".format((a + 18) - at), a + 18)
else:
    print("Voce se alista esse ano {}.".format(a+18))
