# Henry WiersGalla Lillian Anderson 1.3.4 iPython log


def food_id(food):
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            print('Citrus, Fruit')
            return 'Citrus, Fruit'
        else:
            print('Not Citrus, Fruit')
            return 'Not Citrus, Fruit'
    else:
        if food in starchy:
            print('Starchy, NOT Fruit')
            return 'Starchy, NOT Fruit'
        else:
            print('NOT Starchy, NOT Fruit')
            return 'NOT Starchy, NOT Fruit'


food_id('banana')
print('new program')


def food_id_test():

    works = True

    if food_id('orange') != 'Citrus, Fruit':
        works = False
        print('orange bug in food_id()')
    if food_id('banana') != 'Not Citrus, Fruit':
        works = False
        print('banana bug in food_id()')
    if works:
        print('All good!')

food_id_test()

print('new program')
def number_output(value):
    number = 4
    print('I have a number between 1 and 4 inclusive')
    if value < number:
        print(value, ' is too low - my number was ',number,)
    if value > number:
        print(value, ' is too high - my number was ',number,)
    if value == number:
        print('Right on! I was number ',number,)
number_output(4)

print('new program')
def quiz_decimal(digit):
    print('Type a number between 4 and 4.1:')
    if digit <= 4.1 or digit >= 4:
        print('Good! 4 < ', digit, ' < 4.1')
    if digit > 4.1:
        print('No,', digit, 'is greater than 4.1')
    if digit < 4:
        print('No,',digit, 'is less than 4')
quiz_decimal(4.05)