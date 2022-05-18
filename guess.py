import random

while True:
    secret_number = random.randint(1, 100)
    point = 100

    while True:
        print(f'Your score is {point}')
        subtraction=10
        user_guess = int(input('Guess a number'))
        if secret_number == user_guess:
            print('You correctly guessed the number {}'.format(secret_number))
            break
        point -= 10
        if secret_number > user_guess:
            print('you guessed too low')
        else:
            print('you guessed too high')
    answer = input('Play again?')
    if answer not in ('y','Y','yes','YES'):
        break
print('Goodbye')
l=[1,2,3,4]