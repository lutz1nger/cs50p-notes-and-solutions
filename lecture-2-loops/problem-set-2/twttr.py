def main():
    msg = input('Input: ')
    new_msg= ''
    for char in msg:
        if char.lower() not in ['a','e','i','o','u']:
            new_msg += char
    print(f'Output: {new_msg}')

main()
