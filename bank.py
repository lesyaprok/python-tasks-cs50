def main():
    greeting = input("Hey!\n")
    print(getMoney(greeting))

def getMoney(greeting):
    greeting = greeting.lower().strip()
    
    if greeting.startswith("hello"):
        return "$0"
    elif greeting[0] == "h":
        return "$20"
    else:
        return "$100"

main()