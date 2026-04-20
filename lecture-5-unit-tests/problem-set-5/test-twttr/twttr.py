def main():
    print(shorten(input('Input: ')))


def shorten(word):
    new_msg= ''
    for char in word:
        if char.lower() not in ['a','e','i','o','u']:
            new_msg += char
    return new_msg


if __name__ == "__main__":
    main()
