def main():
    names = []

    while True:
        try:
            names.append(input('Name: '))
        except EOFError:
            if len(names) == 1:
                print(f'\nAdieu, adieu, to {names[0]}')
            elif len(names) == 2:
                print(f'\nAdieu, adieu, to {names[0]} and {names[1]}')
            else:
                names_str = ''
                for i in range(len(names)-1):
                    names_str += str(names[i])+', '
                print(f'\nAdieu, adieu, to {names_str}and {names[-1]}')
            break

main()
