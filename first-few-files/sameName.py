# local and global vars with the same var name


def spam():
    eggs = 'spam local'
    print(eggs)  # prints 'spam local'


def bacon():
    eggs = 'bacon local'
    print(eggs)  # prints 'bacon local'


eggs = 'global'
spam()
bacon()
print(eggs)  # prints global


