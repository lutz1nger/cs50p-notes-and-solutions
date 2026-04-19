def main():
    time = input('What time is it? ')
    if 7 <= convert(time) <= 8:
        print('breakfast time')
    elif 12 <= convert(time) <= 13:
        print('lunch time')
    elif 18 <= convert(time) <= 19:
        print('dinner time')

def convert(time):
    hour, minutes = time.strip().split(':')

    if hour == '0' or hour == '00':
        h = 0
    else:
        if hour.startswith('0'):
            h = float(hour.replace('0',''))
        else:
            h = float(hour)

    if minutes == '00':
        m = 0
    else:
        if minutes.startswith('0'):
            m = float(minutes.replace('0',''))/60
        else:
            m = float(minutes)/60
    return h+m

if __name__ == "__main__":
    main()
