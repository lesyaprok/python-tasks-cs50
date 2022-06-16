from random import randint

def main():
    print(solve_problems(generate_problems()))

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 3:
                return level
        except ValueError:
            continue

def generate_integer(level):
    try:
        if level == 1:
            random_int = randint(0, 9)
        elif level == 2:
            random_int = randint(10, 99)
        elif level == 3:
            random_int = randint(100, 999)
        return random_int
    except ValueError:
        raise ValueError

def generate_problems():
    level = get_level()
    problems = {}
    for i in range(10):
        while len(problems) < 10:
         a = generate_integer(level)
         b = generate_integer(level)
         problems[f"{a} + {b} = "] = a + b
    return problems

def solve_problems(problems):
    score = 0
    for problem in problems:
        tries = 3
        while True:
            if tries <= 0:
                print(problem + str(problems[problem]))
                break
            try:
                answer = int(input(problem))
                if answer == problems[problem]:
                    score += 1
                    break
                elif answer != problems[problem] and tries > 0:
                    tries -= 1
                    print("EEE")
                    continue
            except ValueError:
                tries -= 1
                print("EEE")
                continue
    return f"Score: {score}"

if __name__ == "__main__":
    main()