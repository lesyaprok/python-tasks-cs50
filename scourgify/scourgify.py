import sys
import csv

def main():
    files = get_files()
    convert_input(files)

def get_files():
    args = sys.argv[1:]
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    else:
        return args

def convert_input(files):
    [input_file, output_file] = files
    try:
        with open(input_file, newline = "") as infile, open(output_file, "w", newline = "") as outfile:
            reader = csv.reader(infile)
            next(reader, None)

            headers = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames = headers)
            writer.writeheader()

            for r in reader:
                last, first = r[0].split(", ")
                house = r[1]
                writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
