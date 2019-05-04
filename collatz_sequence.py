def collatz(number):
    if number % 2 == 0:
        res = number // 2
        print(res)
        return res
    elif number % 2 == 1:
        res = 3 * number + 1
        print(res)
        return res


try:
    userNum = int(input('Enter a number: '))
    while userNum != 1:
        userNum = collatz(int(userNum))
except ValueError:
    print('Value Error - please enter an integer value')

