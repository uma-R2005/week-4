# Week 4 - Python Projects (Regex & Text Processing)

This repository contains multiple Python mini-projects based on regular expressions and text processing.  
Each project demonstrates practical applications of regex in real-world scenarios.

---

## Projects Included

### 1. Email Validator
- Description: Reads a list of email addresses from a file and validates them using regex.
- File: `email_validator.py`
- Input File: `emails.txt`
- Features:
  - Identifies valid and invalid email addresses.
  - Prints results in a clear format.

---

### 2. Log Analyzer
- Description: Analyzes server log files to extract IP addresses and error codes.
- File: `log_analyzer.py`
- Input File: `access.log`
- Features:
  - Counts total requests.
  - Identifies unique IPs.
  - Extracts error codes (404, 500, 403).
  - Provides detailed mapping of IP → Error Code → Log Entry.

---

### 3. Phone Number Extractor
- Description: Extracts phone numbers from a text file containing mixed content.
- File: `phone_extractor.py`
- Input File: `contacts.txt`
- Features:
  - Detects different phone number formats (local, international, old formats).
  - Displays extracted phone numbers in a clean list.

---

### 4. Password Strength Checker
- Description: Checks the strength of a password based on multiple conditions.
- File: `password_checker.py`
- Features:
  - Checks for:
    - Length ≥ 8
    - Uppercase and lowercase letters
    - Numbers
    - Special characters
  - Provides feedback and categorizes password as Weak, Moderate, or Strong.

---

### 5. Resume Parser
- Description: Extracts useful details like name, email, phone number, and skills from a resume text file.
- File: `resume_parser.py`
- Input File: `resume.txt`
- Features:
  - Extracts candidate’s Name, Email, Phone Number, and Skills.
  - Demonstrates regex-based parsing for structured text.

