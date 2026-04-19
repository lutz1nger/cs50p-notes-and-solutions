def main():
    camel_name = input('camelCase: ')

    snake_name = ''
    for char in camel_name:
        if char.islower():
            snake_name += char
        else:
            snake_name += '_'+char.lower()

    print(f'snake_case: {snake_name}')
main()
