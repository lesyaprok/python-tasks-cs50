import sys

def main():
    print(count_file_lines(get_file_name()))

def get_file_name():
    path = sys.argv[1:]
    if len(path) == 0:
        sys.exit("Too few command-line arguments")
    elif len(path) > 1:
        sys.exit("Too many command-line arguments")
    elif not path[0].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        return path[0]

def count_file_lines(path):
    count = 0
    try:
        with open(path) as file:
            for line in file:
                line = line.rstrip().strip()
                if not (len(line) == 0 or line.startswith("#")):
                    count += 1
            return count
    except FileNotFoundError:
         sys.exit("File doesn't exist")

if __name__ == "__main__":
    main()