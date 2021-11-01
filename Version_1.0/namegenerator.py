import random
name = ["Jonas", "Oliwer", "Greger"]
for x in range(9999999 ** 2):
    x = input('Skriv "starta" för att starta namngenerator: ')
    if x == "starta":
        print(random.choice(name))
