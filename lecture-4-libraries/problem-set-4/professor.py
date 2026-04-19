import random


def main():
    level = get_level()
    numbers = [generate_integer(level) for i in range(20)]
    s = 0

    for i in range(0,20,2):
        counter = 0
        while True:
            result = input(f'{numbers[i]} + {numbers[i+1]} = ')
            try:
                if counter == 2:
                    print(f'{numbers[i] + numbers[i+1]}')
                    break
                elif int(result) == (numbers[i] + numbers[i+1]):
                    s += 1
                    break
                else:
                    print('EEE')
                    counter += 1
                    pass
            except:
                print('EEE')
                counter += 1
                pass

    print(f'Score: {s}')


def get_level():
    while True:
        level = input('Level: ')
        try:
            if int(level) in [1,2,3]:
                return int(level)
        except ValueError:
            pass

def generate_integer(level):
    min = {
        1: 0,
        2: 10,
        3: 100,
    }


    max = {
        1: 9,
        2: 99,
        3: 999,
    }

    return random.randint(min[level],max[level])


if __name__ == "__main__":
    main()
