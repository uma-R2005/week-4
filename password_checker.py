# password_checker.py
import re

def check_password(password):
    reasons = []
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
        reasons.append("✔ Length OK (>=8)")
    else:
        reasons.append("✘ Too short (<8)")

    # Uppercase
    if re.search(r'[A-Z]', password):
        score += 1
        reasons.append("✔ Contains uppercase")
    else:
        reasons.append("✘ Missing uppercase")

    # Lowercase
    if re.search(r'[a-z]', password):
        score += 1
        reasons.append("✔ Contains lowercase")
    else:
        reasons.append("✘ Missing lowercase")

    # Digit
    if re.search(r'\d', password):
        score += 1
        reasons.append("✔ Contains digit")
    else:
        reasons.append("✘ Missing digit")

    # Special character
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
        reasons.append("✔ Contains special character")
    else:
        reasons.append("✘ Missing special character")

    return score, reasons


if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    score, feedback = check_password(pwd)

    print("\n=== Password Strength Report ===")
    print("Score:", score, "/ 5")
    for r in feedback:
        print("-", r)

    if score == 5:
        print("✅ Strong Password!")
    elif score >= 3:
        print("⚠ Moderate Password. Improve it.")
    else:
        print("❌ Weak Password!")