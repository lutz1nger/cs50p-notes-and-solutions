import random

def main():
    guess(set_level())

def set_level():
    while True:
        level = input('Level: ')
        try:
            if int(level) > 0:
                return random.randint(1, int(level))
        except ValueError:
            pass

def guess(number):
    while True:
        guess = input('Guess: ')
        try:
            if int(guess)>0:
                if int(guess) == number:
                    print('Just right!')
                    break
                elif int(guess) > number:
                    print('Too large!')
                else:
                    print('Too small!')
        except ValueError:
            pass

main()
