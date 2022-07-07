import re

def main():
    ip_address = input("IPv4 Address: ")
    print(validate(ip_address))

def validate(ip):
    if re.search(r"(\b(25[0-5])\b|\b(2[0-4][0-9])\b|\b(1[0-9][0-9])\b|\b([1-9][0-9])\b|\b[0-9]\b)\.(\b(25[0-5])\b|\b(2[0-4][0-9])\b|\b(1[0-9][0-9])\b|\b([1-9][0-9])\b|\b[0-9]\b)\.(\b(25[0-5])\b|\b(2[0-4][0-9])\b|\b(1[0-9][0-9])\b|\b([1-9][0-9])\b|\b[0-9]\b)\.(\b(25[0-5])\b|\b(2[0-4][0-9])\b|\b(1[0-9][0-9])\b|\b([1-9][0-9])\b|\b[0-9]\b$)", ip):
        return True
    return False

if __name__ == "__main__":
    main()
