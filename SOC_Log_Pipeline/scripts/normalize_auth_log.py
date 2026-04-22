import re
import csv

INPUT_FILE = "auth.log"
OUTPUT_FILE = "normalized_auth.csv"

patterns = [
    # SSH failed password
    ("ssh_failed", re.compile(r'^(?P<ts>[\d\-T:\.+]+)\s+\S+\s+sshd\[\d+\]: Failed password for (invalid user )?(?P<user>\S+) from (?P<ip>\S+)')),

    # SSH invalid user
    ("ssh_invalid_user", re.compile(r'^(?P<ts>[\d\-T:\.+]+)\s+\S+\s+sshd\[\d+\]: Invalid user (?P<user>\S+) from (?P<ip>\S+)')),

    # SSH accepted
    ("ssh_success", re.compile(r'^(?P<ts>[\d\-T:\.+]+)\s+\S+\s+sshd\[\d+\]: Accepted password for (?P<user>\S+) from (?P<ip>\S+)')),

    # Sudo command
    ("sudo_command", re.compile(r'^(?P<ts>[\d\-T:\.+]+)\s+\S+\s+sudo:\s+(?P<user>\S+)\s+:.*COMMAND=(?P<cmd>.+)$')),

    # Cron
    ("cron_activity", re.compile(r'^(?P<ts>[\d\-T:\.+]+)\s+\S+\s+CRON\[\d+\]:.*session opened for user (?P<user>\S+)'))
]

with open(INPUT_FILE, "r") as infile, open(OUTPUT_FILE, "w", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=[
        "timestamp", "event_type", "username", "source_ip", "command", "raw_message"
    ])
    writer.writeheader()

    for line in infile:
        for event_type, pattern in patterns:
            m = pattern.search(line)
            if m:
                writer.writerow({
                    "timestamp": m.groupdict().get("ts"),
                    "event_type": event_type,
                    "username": m.groupdict().get("user"),
                    "source_ip": m.groupdict().get("ip"),
                    "command": m.groupdict().get("cmd"),
                    "raw_message": line.strip()
                })
                break

print("[+] Normalized auth.log written to normalized_auth.csv")

