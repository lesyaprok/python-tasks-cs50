import inflect

def main():
    print(adieu())

def adieu():
    names = []
    while (True):
        try:
            names.append(input("Adieu, adieu, to "))
        except EOFError:
            break
    p = inflect.engine()
    return f"Adieu, adieu, to {p.join(names)}"

main()