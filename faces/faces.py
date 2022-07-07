def main():
    text = input('Enter your message: ')
    print(convert(text))

def convert(str):
    return str.replace(':)', '\U0001F642').replace(':(', '\U0001F641')

main()

