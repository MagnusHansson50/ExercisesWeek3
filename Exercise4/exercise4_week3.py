print("Del a")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)

print("Del b")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

print("Del c")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if 3 <= x <= 5:
            s += "#"
        else:
            s += "."
    print(s)

print("Del d")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3 or y == 3:
            s += "#"
        else:
            s += "."
    print(s)

print("Del e")
for y in range(1, 7):
     s = ""
     for x in range(1, 9):
         if x == 5:
             s += "#"
         elif x == 7 - y:
             s += "#"
         else:
             s += "."
     print(s)

print("Del f")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y or x == 7 - y:
            s += "#"
        else:
            s += "."
    print(s)

print("Del g")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x % 2 != 0:
            s += "#"
        else:
            s += "."
    print(s)

print("Del h")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if (y == 2 or y == 5) and (2 <= x <= 7):
            s += "#"
        elif (y > 2 and y < 5) and (x == 2 or x == 7):
            s += "#"
        else:
            s += "."
    print(s)

print("Del i")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if (x - y) % 3 == 0:
            s += "."
        elif (x - y) % 3 == 1:
            s += "#"
        else:
            s += "0"
    print(s)

print("Del j")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if (1 <= y <= 3) and (x == 3 or x == 6):
            s += "#"
        elif (5<= y <= 6) and ((y + x) % 2 == 1):
            s += "#"
        else:
            s += "."
    print(s)