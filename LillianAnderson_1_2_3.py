# Lillian Anderson  1.3.3 iPython log

a = 3

print(a ** 2)

print(a == 3)

print(a+1 >= 2 and a**2 != 5)

print(a**2 >= 9 and not a>3)

print(a+2 == 5 or a-1 != 3)

print("shid")

x, y = (90, 115)
print(x)

print(50<x and x<80 and 30<=y and y<=45)

print(x>40 and x<130 and y<120 and y>100)

def age_limit_output(age):
    """Step 6a if-else example"""
    age_limit = 13
    if age < age_limit:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
        print('Minimum age is', age_limit)
age_limit_output(70)

def report_grade (percent):
    """Step 6a if-else"""
    if percent>=80:
        print("A grade of " + str(percent) + " indicates mastery. Keep up the good work!")
    else:
        print("A grade of " + str(percent) + " does not indicate mastery. Seek extra practice or help.")
report_grade(99)

print('t' in 'string')
print('T' in 'string')
print(3 in [1,2,3])
print('3' in [1,2,3])

def vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        print(True)
    else:
        print(False)