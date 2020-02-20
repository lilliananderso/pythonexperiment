some_values = ('a', 'b', 3)

print(some_values)
print(some_values[0:2])

print(some_values[0])
print(some_values[1])
print(some_values[2])

a = 10
tup = (9, a, 11)
print(tup)

a = 15
print(a)

print(tup)

print(tup[1] == 10)
print(tup[1])

values = ['a', 'b', 3]
print(values[1:])

print(values[2])
values[2] = 4
print(values[2] == 4)

values = values + [4, 5]
print(values)

values.append([6, 7])
print(values)

a = 6
a *= 3
print(a)


def roll_14s_dice():

    dicevalues = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    import random
    random.choice(dicevalues)
    d = random.randint(2, 14)

    print(d)

roll_14s_dice()


def roll_two_dice():
    dicevalues = [1, 2, 3, 4, 5, 6]
    import random
    random.choice(dicevalues)
    d = random.randint(1, 6)
    e = random.randint(1, 6)

    print(d + e)

roll_two_dice()

def guess_letter():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    import random
    random.choice(letters)
    a = random.randint(0, 26)
    b = letters[a]

    print(b)

guess_letter()
