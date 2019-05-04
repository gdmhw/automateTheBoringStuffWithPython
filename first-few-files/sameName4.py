def spam(divide_by):
    try:
        return 42/divide_by
    except ZeroDivisionError:  # check for dividing by zero
        print('Error - Invalid Argument')


#  test cases for spam function - dividing by a number

print(spam(2))
print(spam(21))
print(spam(4))
print(spam(42))
print(spam(1))
print(spam(0))

