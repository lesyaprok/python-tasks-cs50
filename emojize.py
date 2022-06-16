from emoji import emojize 

def main():
    str_to_emojize = input("Input: ")
    print(emojize_input(str_to_emojize))

def emojize_input(str):
    return emojize(str)

main()