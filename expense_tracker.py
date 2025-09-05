import argparse, json, os
from collections import defaultdict

FILE = "expenses.json"

def load(): return json.load(open(FILE)) if os.path.exists(FILE) else []
def save(data): json.dump(data, open(FILE, "w"), indent=2)

def add(a, c, d):
    data = load(); data.append({"amount": a, "category": c, "desc": d}); save(data)
    print(f"✅ Added {a} in {c} ({d})")

def list_all():
    data = load()
    if not data: print("No expenses yet."); return
    for i, e in enumerate(data, 1):
        print(f"{i}. {e['amount']} - {e['category']} ({e['desc']})")

def summary():
    totals = defaultdict(float)
    for e in load(): totals[e['category']] += e['amount']
    if not totals: print("No expenses to summarize."); return
    [print(f"{k}: {v}") for k, v in totals.items()]
    print("Total:", sum(totals.values()))

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd")
    a = sub.add_parser("add")
    a.add_argument("amount", type=float)
    a.add_argument("category")
    a.add_argument("desc")
    sub.add_parser("list")
    sub.add_parser("summary")
    args = p.parse_args()

    if args.cmd == "add": add(args.amount, args.category, args.desc)
    elif args.cmd == "list" or args.cmd is None: list_all()
    elif args.cmd == "summary": summary()
    else: p.print_help()

if __name__ == "__main__": 
    main()
