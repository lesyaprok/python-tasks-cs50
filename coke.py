def main():
    prompt_coins()

def prompt_coins():
    amount = 50
    coins = 0
    while(True):
        if amount <= 0:
            print("Change Owed:", abs(amount))
            break
        print(f"Amount Due: {amount}")
        coins = int(input("Insert Coin: "))
        if (coins != 10 and coins != 25 and coins != 5):
            continue
        amount -= coins

main()