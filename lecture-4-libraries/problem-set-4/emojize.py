import emoji

def main():
    emoji_input = input('Input: ')
    print(f'Output: {emoji.emojize(emoji_input, language='alias')}')

main()
