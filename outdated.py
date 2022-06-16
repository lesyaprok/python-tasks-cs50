def main():
    print(prompt_date())

def prompt_date():
    while True:
        date = input("Date in format m/d/y or month day, year: ")
        format1 = date.split("/")
        format2 = date.split(" ")
        filter(None, format2)
        if len(format1) == 3:
            [m, d, y] = format1
            if m.isalpha() or d.isalpha() or y.isalpha():
                continue
            return check_date([m, d, y])
        elif len(format2) == 3:
            [m, d, y] = format2
            if (m.isdigit() or d.isdigit() or y.isalpha()):
                continue
            return check_date([m, d, y])
        else:
            continue

def check_date(date):
    month, day, year = date
    [day, month, year] = [check_day(day), check_month(month), check_year(year)]
    if day and month and year:
        return f"{year}-{month}-{day}"
    else:
        prompt_date()

def check_day(day):
    try:
        day = int(day.replace(",", ""))
        if 0 < day <= 31:
            return f"{day:02}"
    except:
        return False

def check_month(month):
    try:
        month = int(month)
        if 0 < month <= 12:
            return f"{month:02}"
        else:
            return False
    except:
        return get_number_of_month(month)

def get_number_of_month(month):
    month = month.strip().title()
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    if month in months:
        return f"{(months.index(month) + 1):02}"
    return False

def check_year(year):
    try:
        year = int(year)
        return year
    except:
        return False

main()