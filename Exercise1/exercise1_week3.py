# Del1
# limit = 15
# index = 5
# while index <= limit:
#     print(index)
#     index = index + 2
#
# Del2
# for i in range(10):
#     if i == 5:
#         print("")
#     else:
#         print(i)
#     i = i + 1
#
# Del3
# counter = 0
# for i in range(6):
#     counter += 1
# print(counter)
#
# Del3
#
# x = 0
# y = 1
# while y < 10:
#     if y % 2 == 0:
#         x -= y
#     else:
#         x += y * y
#     y += 1
#     print(f"x: {x} y: {y}")
#
# Del4
#
# message = "its_time_to_get_coding"
# print(message[4:8])

for y in range(2, 8):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)
