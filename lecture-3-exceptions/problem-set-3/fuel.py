def main():
    x = get_int('Fraction: ')

    if x >= 0.99:
        print('F')
    elif x <= 0.01:
        print('E')
    else:
        print(f'{x*100:.0f}%')

def get_int(prompt):
    while True:
        try:
            i,j = input(prompt).split('/')
            if (int(i)/int(j)) > 1 or (int(i)/int(j)) < 0:
                pass
            else:
                return (int(i)/int(j))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except NameError:
            pass

main()
