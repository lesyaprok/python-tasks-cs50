from validator_collection import validators

def main():
    email = input("What's your email address? ")
    print(validate(email))

def validate(mail):
    try:
        validators.email(mail)
        return "Valid"
    except ValueError:
        return "Invalid"

if __name__ == "__main__":
    main()
