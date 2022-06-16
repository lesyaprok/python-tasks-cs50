def main():
    var_name = input("camelCase: ")
    print("snake_case:", to_snake(var_name))

def to_snake(name):
    name = name.strip()
    result = ""
    for i in name:
        if i.islower():
            result += i
        else:
            result += f"_{i.lower()}"
    return result

main()