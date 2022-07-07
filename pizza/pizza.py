import sys
from tabulate import tabulate
import csv

def main():
    data = get_data(get_file())
    print(create_table(data))

def get_file():
    args = sys.argv[1:]
    if len(args) < 1:
        sys.exit("Too few command-line arguments")
    elif len(args) > 1:
        sys.exit("Too many command-line arguments")
    elif not args[0].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return args[0]

def get_data(file_name):
    lines = []
    try:
        with open(file_name, newline="") as file:
            list = csv.reader(file)
            for row in list:
                lines.append(row)
        return lines
    except FileNotFoundError:
        sys.exit("File doesn't exist")

def create_table(data):
   return tabulate(data, headers="firstrow", tablefmt="grid")

if __name__ == "__main__":
    main()