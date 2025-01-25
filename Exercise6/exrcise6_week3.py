todo_list = []
done_list = []

while True:
    print("1. Se innehållet i din lista")
    print("2. Lägg till nya punkter i din lista")
    print("3. Markera som klar.")
    print("4. Klargjorda saker.")
    print("5. Avsluta.")
    alternativ = input("Välj ett altenativ: ")
    try:
        alternativ = int(alternativ)
        if alternativ == 1:
            if len(todo_list) > 0:
                for todo in todo_list:
                    print("+ " + todo)
            else:
               print("Listan är tom")
        elif alternativ == 2:
            add_to_list = input("Skriv in en ny sak du måste komma ihåg att göra: ")
            todo_list.append(add_to_list)
            print(f"Ok, lade till {add_to_list} i listan.")
        elif alternativ == 3:
            remove_from_list = input("Vilken sak är du klar med? ")
            todo_list.remove(remove_from_list)
            done_list.append(remove_from_list)
            print(f"Ok, tog bort {remove_from_list} från listan.")
        elif alternativ == 4:
            if len(done_list) > 0:
                for done in done_list:
                    print("+ " + done)
            else:
                print("Listan är tom")
        elif alternativ == 5:
            break
        else:
            print("Ogiltigt värde, försök igen.")
    except ValueError:
        print("Det är inget giltigt alternativ, försök igen")


