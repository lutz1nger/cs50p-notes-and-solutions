def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:

        try:
            x,y,z = (input('Date: ').strip().replace('/',' ')).split(' ')

            if x in months and y[-1] == ',' and int(y.replace(',','')) <=31:
                print(f'{z}-{int(months.index(x))+1:02d}-{int(y.replace(',','')):02d}')
                break
            elif int(x) <= 12 and int(y) <= 31:
                print(f'{z}-{int(x):02d}-{int(y):02d}')
                break
        except NameError:
            pass
        except ValueError:
            pass

main()
