# log_analyzer.py
import re

def analyze_logs(filename):
    with open(filename, "r") as f:
        logs = f.readlines()
    
    ips = []
    errors = []
    detailed = []

    for line in logs:
        ip = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
        code = re.findall(r'\s(404|500|403)\s', line)
        if ip:
            ips.extend(ip)
        if code:
            errors.extend(code)
            detailed.append((ip[0] if ip else "Unknown", code[0], line.strip()))
    
    return ips, errors, detailed


if __name__ == "__main__":
    log_file = input("Enter log file name: ")
    ips, errors, details = analyze_logs(log_file)

    print("\n=== Analysis Report ===")
    print("Total Requests:", len(ips))
    print("Unique IPs:", len(set(ips)))
    print("Total Errors:", len(errors))
    print("Error Codes Count:", {e: errors.count(e) for e in set(errors)})

    print("\nError Details (IP → Code → Log):")
    for d in details:
        print(d[0], "→", d[1], "→", d[2])
