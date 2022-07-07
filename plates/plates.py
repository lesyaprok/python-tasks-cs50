def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return check_len(s) and check_first_letters(s) and (not check_punctuation(s)) and check_digits(s)

def check_len(s):
    return 2 <= len(s) <= 6

def check_first_letters(s):
    return s[0:2].isalpha()

def check_punctuation(s):
    punctuation = "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
    for i in s:
        if i in punctuation:
            return True
    return False

def check_digits(s):
    i = len(s) - 1
    firstDigit = -1
    if s.isalpha():
        return True
    while (s[i].isdigit() and i >= 0):
        firstDigit = s[i]
        i -= 1
    if firstDigit == '0':
        return False
    return s[0:i].isalpha()

main()