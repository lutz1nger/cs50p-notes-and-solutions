def main():
    message = input()
    print(convert(message))

def convert(emoji):
    emoji = emoji.replace(':)','🙂')
    emoji = emoji.replace(':(', '🙁')
    return emoji

main()
