# email_validator.py
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def batch_validate(filename):
    with open(filename, "r") as f:
        emails = f.readlines()
    results = []
    for e in emails:
        e = e.strip()
        if validate_email(e):
            results.append((e, "✅ Valid"))
        else:
            results.append((e, "❌ Invalid"))
    return results

if __name__ == "__main__":
    file_name = input("Enter file with email list: ")
    validations = batch_validate(file_name)
    print("\nResults:")
    for email, status in validations:
        print(email, "->", status)
