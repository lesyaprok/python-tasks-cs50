def main():
    text = input('What do you want to "slow down"?\n')
    print(addPoints(text))

def addPoints(txt):
    return txt.replace(' ', '...')

main()