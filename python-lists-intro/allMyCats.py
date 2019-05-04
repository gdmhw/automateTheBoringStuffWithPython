cat_names = []

while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1))
    print('Enter nothing to stop')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]  # list concatenation


print('The cat names are: ')

for i in range(len(cat_names)):
    print(' ' + cat_names[i] + ' ' + str(i))



