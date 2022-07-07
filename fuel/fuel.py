def main():
    print(fuel_in_tank(prompt_user_input))

def fuel_in_tank(prompt_user_input):
    while True:
        try:
            fraction = prompt_user_input()
            if fraction:
                [x, y] = fraction
                if x > y:
                    continue
            else:
                continue
            percentage = round(x / y * 100)
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{percentage}%"
        except (ZeroDivisionError, ValueError):
            continue

def prompt_user_input():
    try:
        fraction = input("Fraction: ").split("/")
        [x, y] = [int(fraction[0]), int(fraction[1])]
        return [x,y]
    except ValueError:
        return False

main()