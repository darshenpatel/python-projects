import itertools
import string
import time

def common_words(word: str) -> str | None:
    with open('words.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common match: {match} (#{i})'

def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    characters = string.ascii_lowercase

    if digits:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    attempts: int = 0
    for guess in itertools.product(characters, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)

        if guess == word:
            return f'{word} was cracked in {attempts: ,} guesses.'

        print(guess, attempts)

def main():
    password = input('Password: ')
    print('Searching...')

    start_time: float = time.perf_counter()

    if common_match := common_words(password):
        print(common_match)
    else:
        for i in range(3, 6):
            if cracked := brute_force(password, i, digits=True, symbols=True):
                print(cracked)
                break
            else:
                print('There was no match found')

    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2), 'seconds')


if __name__ == '__main__':
    main()

