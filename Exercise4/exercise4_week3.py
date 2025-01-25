# # Del a
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)

# Del b
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

# Del c
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if 3 <= x <= 5:
            s += "#"
        else:
            s += "."
    print(s)

# Del d
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3 or y == 3:
            s += "#"
        else:
            s += "."
    print(s)

#Del e
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

# Del f
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y or x == 7 - y:
            s += "#"
        else:
            s += "."
    print(s)