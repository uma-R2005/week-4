# phone_extractor.py
import re

def extract_numbers(filename):
    with open(filename, "r") as f:
        text = f.read()
    
    # Regex to capture most phone formats
    pattern = r'(\+?\d{1,3}[- ]?)?(\(?\d{2,4}\)?[- ]?\d{3,5}[- ]?\d{4})'
    matches = re.findall(pattern, text)

    formatted = []
    for m in matches:
        full_num = "".join(m)  # combine groups
        digits = "".join(re.findall(r'\d+', full_num))  # keep only digits
        if len(digits) >= 10:   # valid numbers only
            formatted.append(digits[-10:])  # keep last 10 digits
    
    return set(formatted)

if __name__ == "__main__":
    file_name = input("Enter file with text: ")
    numbers = extract_numbers(file_name)

    print("\n=== Phone Numbers Found ===")
    if numbers:
        for n in numbers:
            print(n)
    else:
        print("No phone numbers found.")
