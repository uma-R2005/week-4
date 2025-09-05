import argparse, requests

API = "http://tinyurl.com/api-create.php"

def shorten(url):
    r = requests.get(API, params={"url": url})
    print("Short URL:", r.text)

def expand(url):
    try:
        r = requests.head(url, allow_redirects=True)
        print("Original URL:", r.url)
    except Exception as e:
        print("Error expanding:", e)

def main():
    p = argparse.ArgumentParser(description="URL Shortener CLI")
    sub = p.add_subparsers(dest="cmd")

    s = sub.add_parser("shorten"); s.add_argument("url")
    e = sub.add_parser("expand"); e.add_argument("url")

    args = p.parse_args()
    if args.cmd == "shorten": shorten(args.url)
    elif args.cmd == "expand": expand(args.url)
    else: p.print_help()

if __name__ == "__main__":
    main()
