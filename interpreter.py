def main():
    expr = input("Expression: ")
    print(calculate(expr))

def calculate(expression):
    x, y, z = expression.split(" ")
    x, z = [float(x), float(z)]
    
    if y == "+":
        return round(x + z, 1)
    elif y == "-":
        return round(x - z, 1)
    elif y == "*":
        return round(x * z, 1)
    elif y == "/":
        return round(x / z, 1)

main()