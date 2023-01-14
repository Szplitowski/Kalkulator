import logging
logging.basicConfig(level=logging.DEBUG)
import math
print(f"Wybierz działanie wpisując odpowiednią liczbę: \nDodawanie - wpisz 1 \nOdejmowanie  - wpisz 2 \nMnożenie - wpisz 3 \nDzielenie  - wpisz 4")
typ = input("Wpisz tutaj:")
if int(typ) > 4:
    print("error")
    exit()
else:
    pass
if typ == "1":
  liczby = []
  n = int(input("Podaj ilość liczb, które chcesz dodać do siebie"))

  for i in range(0, n):
    logging.info('Podaj liczbe nr' + str(i+1))
    item = int(input())
    liczby.append(item)
  logging.info('Wynik tego dodawania to:' + str(sum(liczby)))
  exit()


if typ == "3":
  liczby = []
  n = int(input("Podaj ilość liczb, które chcesz pomnożyć"))

  for i in range(0, n):
    logging.info('Podaj liczbe nr' + str(i+1))
    item = int(input())
    liczby.append(item)
  logging.info('Mnożę liczby:' + str(liczby))
  logging.info('Wynik tego mnożenia to:' + str(math.prod(liczby)))
  exit()


a = input("Podaj a:")
b = input("Podaj b:")
a = int(a)
b = int(b)
if typ == "2":
    logging.info('Odejmuję %s - %s', a, b)
    c = a - b
    logging.info('Wynik to %s', c)
if typ == "4":
    logging.info('Dzielę %s przez %s', a, b)
    c = a / b
    logging.info('Wynik to %s', c)