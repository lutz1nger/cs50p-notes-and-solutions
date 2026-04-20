def main():
    if is_valid(input("Plate: ")):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return start_two_letters(s) and is_alphanumeric(s) and correct_len(s) and no_zero(s) and end_numbers(s)

def start_two_letters(s):
    return s[:2].isalpha()

def is_alphanumeric(s):
    return s.isalnum()

def correct_len(s):
    return 7 > len(s) > 1

def no_zero(s):
    num = ''
    for char in s:
        if char.isnumeric():
            num += char
    if len(num) == 0:
        return True
    else:
        return num[0] != '0'

def end_numbers(s):
    x = 0
    for i in range(len(s)-1):
        if s[i].isnumeric() and s[i+1].isalpha():
            x += 1
    return x == 0
  

if __name__ == "__main__":
    main()
