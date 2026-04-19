def main():
    items = []
    while True:
        try:
            items.append(input().upper().strip())
        except EOFError:
            count = {item: items.count(item) for item in items}
            for key in sorted(count.keys()):
                print(f'{count[key]} {key}')

            break

main()
