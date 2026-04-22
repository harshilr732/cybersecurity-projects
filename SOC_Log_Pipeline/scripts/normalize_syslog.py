import csv
import re
from datetime import datetime

INPUT = "syslog"
OUTPUT = "normalized_syslog.csv"

cron_regex = re.compile(r'CRON\[\d+\]: \((?P<user>[^)]+)\) CMD')

with open(OUTPUT, "w", newline='') as out:
    writer = csv.writer(out)
    writer.writerow(["timestamp", "program", "event_type", "username", "raw_message"])

    with open(INPUT) as f:
        for line in f:
            if "CRON" not in line:
                continue

            match = cron_regex.search(line)
            if not match:
                continue

            try:
                ts = line.split()[0]
                # Already ISO timestamp, no parsing needed
            except:
                continue

            user = match.group("user")

            writer.writerow([
                ts,
                "cron",
                "cron_activity",
                user,
                line.strip()
            ])

print("[+] Normalized syslog written to normalized_syslog.csv")
