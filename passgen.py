import argparse, random, string

def generate(length=12, digits=True, symbols=True):
    chars = string.ascii_letters
    if digits: chars += string.digits
    if symbols: chars += "!@#$%^&*()-_=+[]{}"
    return "".join(random.choice(chars) for _ in range(length))

def main():
    p = argparse.ArgumentParser(description="Password Generator CLI")
    p.add_argument("--length", type=int, default=12, help="Password length")
    p.add_argument("--digits", action="store_true", help="Include digits")
    p.add_argument("--symbols", action="store_true", help="Include symbols")
    p.add_argument("--count", type=int, default=1, help="Number of passwords")
    args = p.parse_args()

    for _ in range(args.count):
        print(generate(args.length, args.digits, args.symbols))

if __name__ == "__main__":
    main()
