from collections import Counter
from datetime import datetime
from itertools import groupby
from operator import itemgetter

log_file_path = "server_logs.txt"

logs = []

with open(log_file_path, 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) != 5:
            print(f"⚠️ Skipping malformed line: {line.strip()}")
            continue
        
        timestamp_str = parts[0] + " " + parts[1]  # combine date and time
        user = parts[2]
        url = parts[3]
        status_str = parts[4]

        try:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            status = int(status_str)
        except ValueError:
            print(f"⚠️ Skipping malformed line (bad date/status): {line.strip()}")
            continue

        hour = timestamp.replace(minute=0, second=0)
        logs.append((hour, user, url, status))

user_counter = Counter(log[1] for log in logs)
page_counter = Counter(log[2] for log in logs)
status_counter = Counter(log[3] for log in logs)

# Sort logs by hour for groupby
logs.sort(key=itemgetter(0))
print("\n🕒 Traffic by Hour (using itertools.groupby):")
for hour, group in groupby(logs, key=itemgetter(0)):
    group_list = list(group)
    print(f"{hour.strftime('%Y-%m-%d %H:00')}: {len(group_list)} requests")

print("\n📈 Most Active Users:")
for user, count in user_counter.most_common(5):
    print(f"{user}: {count} requests")

print("\n📄 Most Visited Pages:")
for page, count in page_counter.most_common(5):
    print(f"{page}: {count} visits")

print("\n🚨 HTTP Status Codes:")
for status, count in status_counter.items():
    print(f"{status}: {count} occurrences")
