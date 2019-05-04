import copy

spam = ['A', 'B', 'C', 'D']

print('Spam List: ' + str(spam))


cheese = copy.copy(spam)

print('Cheese List(copy function used on spam): ' + str(cheese))

cheese[1] = 41

print('Cheese[1] set to 42: ' + str(cheese))

spam2 = [1, 2, 3, [1, 2], 4]
print('Spam2 List: ' + str(spam2))
cheese2 = copy.copy(spam2)
cheese3 = copy.deepcopy(spam2)
print('Cheese 2 (copy of spam 2 using copy.copy()): ' + str(cheese2))
print('Cheese 3 (copy of spam 2 using copy.deepcopy()): ' + str(cheese3))



