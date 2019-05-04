import random

secret_number = random.randint(1, 20)

print('I\'m thinking of a number between 1 and 20')

# ask for a guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secret_number:
        print('Guess is too low')
    elif guess > secret_number:
        print('Guess too high')
    else:  # else if correct number guessed or out of guesses
        break


if guess == secret_number:
    print('Guess of ' + str(secret_number) + ' was correct')
    print('Number of guesses: ' + str(guessesTaken))
else:
    print('Out of guesses, the secret number was ' + str(secret_number))

