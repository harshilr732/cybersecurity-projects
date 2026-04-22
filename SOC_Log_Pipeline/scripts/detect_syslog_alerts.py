import csv

INPUT = "normalized_syslog.csv"
ALERT_FILE = "syslog_alerts.txt"

alerts = []

with open(INPUT) as f:
    reader = csv.DictReader(f)

    for row in reader:
        user = row["username"]
        ts = row["timestamp"]
        msg = row["raw_message"].lower()

        # Suspicious download + execution
        if ("wget" in msg or "curl" in msg):
            if ".sh" in msg or "| bash" in msg:
                alerts.append(
                    f"[HIGH] Suspicious Script Download & Execution | User: {user} | Time: {ts} | Msg: {row['raw_message']}"
                )

        # Execution from temp directories
        if ("/tmp" in msg or "/dev/shm" in msg):
            if "bash" in msg or "sh" in msg:
                alerts.append(
                    f"[MEDIUM] Execution from Temp Directory | User: {user} | Time: {ts} | Msg: {row['raw_message']}"
                )

        # Netcat usage
        if "nc" in msg:
            alerts.append(
                f"[HIGH] Possible Netcat Usage | User: {user} | Time: {ts} | Msg: {row['raw_message']}"
            )

with open(ALERT_FILE, "w") as f:
    for a in alerts:
        f.write(a + "\n")

print(f"[+] Syslog detection complete. Alerts written to {ALERT_FILE}")
