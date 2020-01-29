from __future__ import print_function  # use Python 3.0 printing

a = 3
b = (a ** 2)
print(b)

print("butt stuff")

a == 3
True

a + 1 >= 2 and a ** 2 != 5
True

x, y = (65, 40)
print(x)

var = 50 < x and x < 80 and 30 <= y and y <= 45


def age_limit_output(age):
    """Step 6a if-else example"""
    age_limit = 13
    if age < age_limit:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', age_limit)


age_limit_output(10)
age_limit_output(16)

var = 't' in 'string'
var = True
var = 'T' in 'string'
var = False
var = 3 in [1, 2, 3]
var = True
var = '3' in [1, 2, 3]
var = False
def vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False
letter_in_word ('t', 'secret hangman phrase'):


secret = ['red','red','yellow','yellow','black']
#The color red is in the secret sequence of colors.
hint('green', secret)
#The color green is not in the secret sequence of colors.

secret = ['red','red','yellow','yellow','black']
hint('red', secret)
#The color red is in the secret sequence of colors.
hint('green', secret)
#The color green is not in the secret sequence of colors.

