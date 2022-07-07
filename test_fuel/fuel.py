def main():
    print(get_output())

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        return round(x / y * 100)
    except ValueError:
        raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def get_output():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            return gauge(percentage)
        except (ValueError, ZeroDivisionError):
            continue

if __name__ == "__main__":
    main()