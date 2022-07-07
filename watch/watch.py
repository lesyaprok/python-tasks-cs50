import re

def main():
    html = input("HTML: ")
    print(parse(html))

def parse_src(html):
    if url := re.search(r"src=\"([^\"]+)", html):
        url = url.group(1)
        return url
    else:
        return

def parse_query_param(url):
    if query := re.search(r"https?://(?:www\.)?youtube\.com/embed/(.+)", url):
        query = query.group(1)
        return query
    else:
        return

def parse(html):
    if url := parse_src(html):
        query = parse_query_param(url)
    else:
        return
    if query:
        return f"https://youtu.be/{query}"
    else:
        return

if __name__ == "__main__":
    main()
