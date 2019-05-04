def spam():
    global eggs
    eggs = 'spam'  # this is done globally


def bacon():
    eggs = 'bacon'  # this is done locally


def ham():
    print(eggs)


eggs = 42  # this is the global
spam()  # assign global var
print(eggs)  # prints spam