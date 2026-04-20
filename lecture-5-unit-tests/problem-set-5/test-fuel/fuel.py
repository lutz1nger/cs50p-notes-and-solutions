def main():
    while True:
        try:
            f = convert(input('Fraction: '))
            break
        except:
            pass

    print(gauge(f))
  

def convert(fraction):
    x,y = fraction.split('/')
    if x.isdigit() == False or y.isdigit() == False or int(x) > int(y):
        raise ValueError
    elif int(y) ==  0:
        raise ZeroDivisionError
    else:
        return round(int(x)*100/int(y))


def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f'{percentage:.0f}%'
      

if __name__ == "__main__":
    main()
