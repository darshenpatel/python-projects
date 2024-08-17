from random import randint

lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)
print(f'Guess the number in the range from {lower_num} to {higher_num}.')

while True:
    try: guess = int(input('Guess: '))
    except ValueError as e:
        print(f'Sorry,{e} please enter a valid number.')
        continue

    if guess > random_number:
        print ('The number is lower')
    elif guess < random_number:
        print ('The number is higher')
    else:
        print ('That is the correct number!')
        break
