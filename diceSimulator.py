import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls


def main():
    while True:
        try:
            user_input: str = input("How many dice do you want to roll? ")

            if user_input.lower() == 'exit':
                print('Thank you for playing!')
                break
            print (*roll_dice(int(user_input)), sep=', ')
                # * = unpacking the list

        except ValueError:
            (print('Please enter a number between 1 and 6'))


if __name__ == '__main__':
    main()
