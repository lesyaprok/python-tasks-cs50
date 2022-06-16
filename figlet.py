import sys
import random
import pyfiglet

args = sys.argv[1:]
fonts = pyfiglet.FigletFont.getFonts()
font = ""

if len(args) == 0:
    font = random.choice(fonts)
elif len(args) == 2 and (args[0] == "--font" or args[0] == "-f") and args[1] in fonts:
    font = args[1]
else:
    sys.exit("Error")

def main():
    user_input = input("Input: ")
    print(transform_text(user_input, font))

def transform_text(str, user_font):
    f = pyfiglet.Figlet(font=user_font)
    return f.renderText(str)

main()