import pprint

message1 = 'It was a bright cold day in April, and the ' \
          'clocks were striking thirteen.'
count = {}


def char_count(message):
    for i in message:
        count.setdefault(i, 0)
        count[i] = count[i] + 1
    return count


# cleaner output, keys are sorted with pprint

pprint.pprint(char_count(message1))

# text can be given as a string value
print()
print(pprint.pformat(char_count(message1)))
