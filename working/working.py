import re

def main():
    hours = input("Hours: ").strip()
    print(convert(hours))


def validate_hours(time):
    if not re.search(r"\s(AM|PM)", time):
        return False
    elif ":" in time and re.search(r"\b(((0?[0-9])|1[0-2]):[0-5][0-9])\b", time):
        return True
    elif ":" not in time and re.search(r"0?[0-9]|1[0-2]", time):
        return True
    else:
        return False


def get_time(us_time):
    if "AM" in us_time:
        am_or_pm = "AM"
    else:
        am_or_pm = "PM"

    us_time = us_time.replace("AM", "").replace("PM", "").strip()

    if ":" in us_time:
        hours, minutes = us_time.split(":")
    else:
        hours = us_time
        minutes = "00"

    return [hours, minutes, am_or_pm]


def convert_time(time_data):
    hours, minutes, am_pm = time_data
    if am_pm == "AM" and hours == "12":
        hours = 0
    elif am_pm == "PM" and not hours == "12":
        hours = int(hours) + 12

    return f"{hours:0>2}:{minutes}"


def convert(hours):
    try:
        hours = re.search(r"([^to]+) to (.+)", hours)
        start, finish = hours.group(1), hours.group(2)

        if validate_hours(start) and validate_hours(finish):
            start_data = get_time(start)
            finish_data = get_time(finish)

            converted_start = convert_time(start_data)
            converted_end = convert_time(finish_data)
            
            return f"{converted_start} to {converted_end}"
        else:
            raise ValueError
            return
    except:
        raise ValueError

if __name__ == "__main__":
    main()