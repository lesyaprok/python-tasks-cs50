def main():
    text = input("input: ")
    print(shorten(text))

def shorten(word):
    result = ""
    vowels = "aeiou"
    for i in word:
        low = i.lower()
        if low in vowels:
            continue
        else:
            result += i
    return result

if __name__ == "__main__":
    main()