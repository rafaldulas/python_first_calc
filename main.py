l1=int(input("Wprowadź pierwszą liczbę: "))
l2=int(input("Wprowadź drugą liczbę: "))

print("Wprowadziłeś liczby ", l1, " oraz ", l2)
dzialanie=input("Wybierz operację matematyczną (dodaj, odejmij, pomnoz, podziel): ")
dodawanie = (l1 + l2)
odejmowanie = (l1 - l2)
mnozenie = (l1 * l2)
dzielenie = (l1 / l2)

if dzialanie=="dodaj":
    print("Wynik dodawania wynosi: ", dodawanie)
elif dzialanie=="odejmij":
    print("Wynik odejmowania wynosi: ", odejmowanie)
elif dzialanie=="pomnoz":
    print("Wynik mnożenia wynosi: ", mnozenie)
elif dzialanie=="podziel":
    print("Wynik dzielenia wynosi: ", dzielenie)
else:
    print("Wybierz operację matematyczną ponownie")


print("-------------------------")


