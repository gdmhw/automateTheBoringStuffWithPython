message1 = 'It was a bright cold day in April, and the ' \
          'clocks were striking thirteen.'

count = {}


# setdefault - ensures a key exists

def char_count(message):
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    print(count)


char_count(message1)

