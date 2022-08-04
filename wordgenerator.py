import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

i = 0
randomNickLength = random.randint(3, 10)
suggestedNick = ""

print("\nHere is your suggested nickname:\n")
while i < randomNickLength:
    letterSelector = random.randint(0, 25)
    print(*alphabet[letterSelector])
    i += 1

print("\n")



## Idéer:
## Skapa separata arrays för vokaler och konsonanter. Printa ut på ett grammatiskt korrekt sätt
## Hitta hur man printar en array i en rad (appenda bokstav för bokstav till en string-variabel och printa den)
## Fråga om användaren är nöjd eller vill fortsätta - isåfall loopa programmet
