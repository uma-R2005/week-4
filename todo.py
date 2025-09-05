import argparse, json, os

FILE = "todos.json"

def load(): return json.load(open(FILE)) if os.path.exists(FILE) else []
def save(data): json.dump(data, open(FILE, "w"), indent=2)

def add(task):
    data = load(); data.append({"task": task, "done": False}); save(data)
    print(f"✅ Added: {task}")

def list_tasks():
    data = load()
    if not data: print("No tasks yet."); return
    for i, t in enumerate(data, 1):
        status = "✔" if t["done"] else "✗"
        print(f"{i}. {t['task']} [{status}]")

def mark_done(i):
    data = load()
    if 0 < i <= len(data):
        data[i-1]["done"] = True; save(data); print(f"✔ Marked done: {data[i-1]['task']}")
    else: print("Invalid task number")

def clear(): save([]); print("🗑 Cleared all tasks")

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd")
    a = sub.add_parser("add"); a.add_argument("task")
    d = sub.add_parser("done"); d.add_argument("num", type=int)
    sub.add_parser("list"); sub.add_parser("clear")
    args = p.parse_args()

    if args.cmd=="add": add(args.task)
    elif args.cmd=="list" or args.cmd is None: list_tasks()
    elif args.cmd=="done": mark_done(args.num)
    elif args.cmd=="clear": clear()
    else: p.print_help()

if __name__=="__main__": main()
