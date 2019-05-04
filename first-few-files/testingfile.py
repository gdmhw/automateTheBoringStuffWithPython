import random
import sys


string = ''

for i in range(5):
    print(random.randint(50, 400))
    # string.join(randint(1, 10) + ' ')

print('hello')
print(len('hello'))

round1 = round(10.5)

round2 = round(0.9)

print(round1)
print(round2)

while True:
    print('type exit to exit')
    response = input()
    if response == 'exit':
        print('you have typed exit')
        sys.exit()
    print('You typed ' + response)

