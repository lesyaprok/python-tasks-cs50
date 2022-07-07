def main():
    answer = input("What's the Great Question of Life, the Universe and Everything? ")
    print(isTrue(answer))

def isTrue(answer):
    answer = answer.lower().strip()
    if (answer == "42" or answer == "forty-two" or answer == "forty two"):
        return "Yes"
    else:
        return "No"

main()