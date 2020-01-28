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

age_limit_output(89)