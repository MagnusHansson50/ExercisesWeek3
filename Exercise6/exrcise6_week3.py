todo_list = []
done_list = []

def print_todo_list():
    if len(todo_list) > 0:
        print("Att göra listan")
        i = 1
        for todo in todo_list:
            print(f"{i}. " + todo)
            i += 1
        return True
    else:
        print("Listan är tom")
        return False

def print_done_list():
    if len(done_list) > 0:
        print("Att göra listan")
        i = 1
        for done in done_list:
            print(f"{i}. " + done)
            i += 1
        return True
    else:
        print("Listan är tom")
        return False

while True:
    print("Meny")
    print("1. Se innehållet i din lista")
    print("2. Lägg till nya punkter i din lista")
    print("3. Markera som klar.")
    print("4. Klargjorda saker.")
    print("5. Lägga tillbaka saker ifrån klargjorda listan.")
    print("6. Avsluta.")
    alternativ = input("Välj ett alternativ: ")
    try:
        alternativ = int(alternativ)
        if alternativ == 1:
            print_todo_list()
        elif alternativ == 2:
            add_to_list = input("Skriv in en ny sak du måste komma ihåg att göra: ")
            todo_list.append(add_to_list)
            print(f"Ok, lade till {add_to_list} i listan.")
        elif alternativ == 3:
            if print_todo_list():
                index = input("Vilken sak är du klar med, ange nummer? ")
                if index.isdigit():
                    if 0 < int(index) <= len(todo_list):
                        done_list.append(todo_list[int(index) - 1])
                        removed = todo_list[int(index) - 1]
                        todo_list.pop(int(index) - 1)
                        print(f"Ok, tog bort {removed} från listan.")
                    else:
                        print("Inget giltig nummer!!!")
                else:
                    print("Ingen giltig inmatning")
            else:
                print("Lägg till saker först")
        elif alternativ == 4:
            print_done_list()
        elif alternativ == 5:
            if print_done_list():
                index = input("Vilket nummer i listan vill du lägga tillbaka? ")
                if index.isdigit():
                    if 0 < int(index) <= len(done_list):
                        todo_list.append(done_list[int(index) - 1])
                        done_list.pop(int(index) - 1)
                    else:
                        print("Inget giltig nummer!!!")
                else:
                    print("Ingen giltig inmatning")
            else:
                print("Klarmarkera saker först.")
        elif alternativ == 6:
            break
        else:
            print("Ogiltigt värde, försök igen.")
    except ValueError:
        print("Det är inget giltigt alternativ, försök igen")


