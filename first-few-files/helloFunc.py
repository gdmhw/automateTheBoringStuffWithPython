# Introduction to functions in python
import random


def hello():
    print('Hi!')
    print('Hi!!!')
    print('Hello')


hello()


def say_name(name):
    print('Hello ' + name)


say_name('Grant')


def get_answer(given_number):
    if given_number == 1:
        return 'It is certain'
    elif given_number == 2:
        return 'Decidedly so'
    elif given_number == 3:
        return 'Absolutely'
    elif given_number == 4:
        return 'Nah'
    elif given_number == 5:
        return 'Try again'
    elif given_number == 6:
        return 'Nope'
    elif given_number == 7:
        return 'Ask once more'
    elif given_number == 8:
        return 'Not really'
    elif given_number == 9:
        return 'No'
    else:
        return 'What? This should not be a response whatsoever'


r = random.randint(1, 9)
your_fortune = get_answer(r)
print(your_fortune)

# or use this line as an alternative to the three above..
print(get_answer(random.randint(1, 9)))

