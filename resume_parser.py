# resume_parser.py
import re

def parse_resume(filename):
    with open(filename, "r") as f:
        content = f.read()

    # Extract emails
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

    # Extract phone numbers (10 digits or formats with - / spaces)
    phones = re.findall(r'\+?\d{1,3}?[-.\s]?\(?\d{2,5}\)?[-.\s]?\d{3,5}[-.\s]?\d{4}', content)

    # Extract skills (simple example: Python, Java, SQL, etc.)
    skills_pattern = r'\b(Python|Java|C\+\+|SQL|JavaScript|HTML|CSS|Machine Learning|Data Science)\b'
    skills = re.findall(skills_pattern, content, re.IGNORECASE)

    return emails, phones, skills


if __name__ == "__main__":
    file_name = input("Enter resume text file name: ")
    emails, phones, skills = parse_resume(file_name)

    print("\n=== Resume Parsing Report ===")
    print("Emails Found:", emails if emails else "None")
    print("Phone Numbers Found:", phones if phones else "None")
    print("Skills Found:", set(skills) if skills else "None")
