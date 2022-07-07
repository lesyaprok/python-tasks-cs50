def main():
    fileName = input("File name: ")
    print(getMediaType(fileName))

def getMediaType(file):
    file = file.strip().lower()

    if file.endswith(".gif"):
        return "image/gif"
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        return "image/jpeg"
    elif file.endswith(".png"):
        return "image/png"
    elif file.endswith(".pdf"):
        return "application/pdf"
    elif file.endswith(".txt"):
        return "text/plain"
    elif file.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()