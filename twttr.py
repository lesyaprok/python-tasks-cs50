def main():
    text = input("input: ")
    print(replace_vowels(text))

def replace_vowels(txt):
    result = ""
    vowels = "aeiou"
    for i in txt:
        low = i.lower()
        if low in vowels:
            continue
        else:
            result += i
    return result

main()