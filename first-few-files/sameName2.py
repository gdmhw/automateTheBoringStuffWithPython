def spam():
    global eggs
    eggs = 'spam'


eggs = 'global'
print(eggs)  # prints global
spam()  # assign to global variable
print(eggs)  # print spam

