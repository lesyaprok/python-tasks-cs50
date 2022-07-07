import re

def main():
    text = input("Text: ")
    print(count(text))

def count(text):
    return len(re.findall(r"\b[^a-zA-Z]?um[^a-zA-Z]?\b", text, re.IGNORECASE))

if __name__ == "__main__":
    main()
