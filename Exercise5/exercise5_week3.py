import random

secret = random.randint(1, 100)
gissning = 0
antal_gissningar = 0

while gissning != secret:
    gissning = input("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är? ")

    try:
        gissning = int(gissning)
        antal_gissningar += 1

        if gissning < secret:
            print("Nej, det är för lågt.")
            if abs(gissning - secret) <= 5:
                print("Det börjar brännas!!!")
        elif gissning > secret:
            print("Nej, det är för högt.")
            if abs(gissning - secret) <= 5:
                print("Det börjar brännas!!!")
        else:
            print(f"Det är rätt!!! Du gjorde det på {antal_gissningar} gissningar.")
            break
    except ValueError:
        print("Det är inget tal, försök igen")
