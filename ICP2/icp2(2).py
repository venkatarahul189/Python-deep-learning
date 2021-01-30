set = 0
a = int(input('num:'))
while a != 0:
    if (a % 2) == 0:
        a = a/2
        set = set + 1
    else:
        a = a - 1
        set = set + 1
print(set)