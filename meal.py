def main():
    time = input("What time is it? ")
    result = timeToEat(convert(time))
    if result != "wait":
        print(result)

def convert(time):
    isPM = False
    isAM = False

    if time.endswith("p.m."):
        isPM = True
        time = time.split(" ")[0]
    elif time.endswith("a.m."):
        isAM = True
        time = time.split(" ")[0]

    hours, minutes = time.split(":")

    if isPM and float(hours) < 12:
        hours = float(hours) + 12
    elif isAM and float(hours) == 12:
        hours = 0

    return float(hours) + (int(minutes) / 60)

def timeToEat(time):
    if 7 <= time <= 8:
        return "breakfast time"
    elif 12 <= time <= 13:
        return "lunch time"
    elif 18 <= time <= 19:
        return "dinner time"
    else:
        return "wait"

if __name__ == "__main__":
    main()