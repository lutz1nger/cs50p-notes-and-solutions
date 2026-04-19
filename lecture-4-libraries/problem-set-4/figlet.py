import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        figlet.setFont(font = random.choice(figlet.getFonts()))
    elif len(sys.argv) == 3 and sys.argv[1] == '-f' or sys.argv[1] == '--font':
            try:
                figlet.setFont(font = sys.argv[2])
            except:
                 sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')

    msg = input('Input: ')

    print('Output:')
    print(figlet.renderText(msg))

main()
