print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")

belopp = 0
summan = 0
dricks = 10

while belopp != 'quit':
    belopp = input("Skriv in ett belopp: ")
    if belopp.isdigit():
        summan += int(belopp)
while True:
    antal = input("Hur många är ni? ")
    try:
        antal = int(antal)
        break
    except ValueError:
        print("Det är inget giltigt nummer!")

dricks = input("Hur mycket dricks vill ni ge? ")
if dricks.isdigit():
    dricks = int(dricks)
    summan = summan + summan * (dricks / 100)
else:
    summan = summan + summan * (10 / 100)

per_person = summan / int(antal)
print(f"Det blir {summan} kr totalt, alltså {per_person} per person. Välkommen åter!")
