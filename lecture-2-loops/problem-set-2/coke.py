def main():
    i = 50
    while i > 0:
        print(f'Amount Due: {i}')
        j = input('Insert Coin: ')
        if j == '5' or j == '10' or j == '25':
            i -= int(j)

    print(f'Change Owed: {abs(i)}')

main()
