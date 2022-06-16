import random
import sys

def main():
    guessing_game()

def guess(number):
    while True:
        try:
            n = int(input("Guess a number: "))
            if n <= 0:
                continue
            elif n < number:
                print("Too small!")
            elif n > number:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()
        except ValueError:
            continue

def guessing_game():
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            if number > 0:
                break
        except ValueError:
            continue
    random_integer = random.randint(1, number)
    guess(random_integer)

main()