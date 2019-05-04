# function takes in a list, returns a string with all items separated by a comma
# except for last item which is preceded by an 'and';
# for lists of length 1, just print the single list item;
# for lists of length 2, print 2 items separated by an 'and';


def comma_space(list):
    if len(list) == 1:
        print(list[0])
    elif len(list) == 2:
        print(list[0] + ' and ' + list[1])
    else:
        for i in list[:-1]:
            print(i + ', ', end='')  # end needed so list items not printed on new line
        print("and " + list[-1])


list1 = ['Apple', 'Bloomberg', 'CNN', 'Duolingo']
comma_space(list1)
list2 = ['Apple']
comma_space(list2)
list3 = ['Apple', 'Bloomberg']
comma_space(list3)



