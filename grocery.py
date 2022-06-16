def main():
    make_list()

def make_list():
    products_list = {}
    while True:
        try:
            item = input().upper().strip()
            products_list[item] += 1
        except KeyError:
            products_list[item] = 1
        except EOFError:
            return show_list(products_list)

def show_list(products_list):
    sorted_list = sorted(products_list.items())
    for item in sorted_list:
        print(f"{item[1]} {item[0]}")

main()