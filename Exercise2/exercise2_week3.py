# Del 1a
answer = 0
for i in range(11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))

# Del 1b
answer = 0
for i in range(101):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))

# Del 1c
i = 1
answer = 0
while i <= 100:
    answer += i
    i += 1
print("Summan av talen 1 till 10 är: " + str(answer))

# Del 2
lista = [1, -2, 3, -2, 4, -3]
summan = sum(lista)
print(f"Summan av alla tal i listan är: {summan}")

summan = 0
for tal in lista:
    summan += tal
print(f"Summan av alla tal i listan är: {summan}")

# Del 3
filmer = ["Top Gun", "Die Hard", "Polisskolan", "Minioner"]
print(filmer)
filmer.append("Fellowship of the ring")
print(filmer)
filmer.insert(0, "The two towers")
print(filmer)
index = filmer.index("Fellowship of the ring")
print(f"Fellowship of the ring har index {index} i listan")
filmer.remove("Die Hard")
print(filmer)
index = filmer.index("Fellowship of the ring")
print(f"Fellowship of the ring har index {index} i listan")
langd = len(filmer)
print(f"Längden på listan är {langd}")
filmer.reverse()
print(filmer)
filmer.sort()
print(filmer)
