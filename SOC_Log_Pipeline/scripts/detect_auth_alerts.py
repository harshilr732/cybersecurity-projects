import csv
from datetime import datetime, timedelta
from collections import defaultdict

INPUT_FILE = "normalized_auth.csv"
ALERT_FILE = "auth_alerts.txt"

BRUTE_FORCE_THRESHOLD = 5
BRUTE_FORCE_WINDOW_MINUTES = 5
SUCCESS_AFTER_FAIL_THRESHOLD = 3

failed_by_ip = defaultdict(list)
failed_by_user = defaultdict(list)

alerts = []
alerted_ips = set()        # prevents repeated brute force alerts
bruteforce_ips = set()     # track IPs that triggered brute force
seen_log_access = set()    # deduplicate log access alerts

with open(INPUT_FILE, newline='') as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            ts = datetime.fromisoformat(row["timestamp"])
        except:
            continue

        event = row["event_type"]
        user = row["username"]
        ip = row["source_ip"]
        cmd = row.get("command", "")

        # =========================
        # TRACK FAILED ATTEMPTS
        # =========================
        if event == "ssh_failed":
            if ip:
                failed_by_ip[ip].append(ts)
            if user:
                failed_by_user[user].append(ts)

        # =========================
        # SSH BRUTE FORCE DETECTION
        # =========================
        if event == "ssh_failed" and ip:
            recent = [t for t in failed_by_ip[ip]
                      if ts - t <= timedelta(minutes=BRUTE_FORCE_WINDOW_MINUTES)]

            if len(recent) >= BRUTE_FORCE_THRESHOLD and ip not in alerted_ips:
                alerts.append(
                    f"[HIGH] SSH Brute Force | IP: {ip} | Attempts: {len(recent)} | Window: {BRUTE_FORCE_WINDOW_MINUTES} min | Time: {ts}"
                )
                alerted_ips.add(ip)
                bruteforce_ips.add(ip)

        # =========================
        # SUCCESS AFTER FAILURES
        # =========================
        if event == "ssh_success" and user:
            recent_user_fails = [t for t in failed_by_user[user]
                                 if ts - t <= timedelta(minutes=10)]

            if len(recent_user_fails) >= SUCCESS_AFTER_FAIL_THRESHOLD:
                alerts.append(
                    f"[HIGH] SSH Success After Failures | User: {user} | Failures: {len(recent_user_fails)} | IP: {ip} | Time: {ts}"
                )

        # =========================
        # CRITICAL: SUCCESS AFTER BRUTE FORCE (CORRELATION)
        # =========================
        if event == "ssh_success" and ip:
            if ip in bruteforce_ips:
                alerts.append(
                    f"[CRITICAL] Possible Account Compromise | IP: {ip} | User: {user} | Time: {ts}"
                )

        # =========================
        # SENSITIVE FILE ACCESS
        # =========================
        if event == "sudo_command" and cmd:
            if "/etc/shadow" in cmd or "/etc/passwd" in cmd:
                alerts.append(
                    f"[HIGH] Sensitive File Access | User: {user} | Command: {cmd} | Time: {ts}"
                )

        # =========================
        # SSH SERVICE MODIFICATION (PERSISTENCE)
        # =========================
        if event == "sudo_command" and cmd:
            if "systemctl enable ssh" in cmd or "systemctl start ssh" in cmd:
                alerts.append(
                    f"[MEDIUM] SSH Service Modification | User: {user} | Command: {cmd} | Time: {ts}"
                )

        # =========================
        # LOG ACCESS (DEDUPLICATED)
        # =========================
        if event == "sudo_command" and cmd:
            if "tail -n" in cmd and "/var/log" in cmd:
                key = (user, cmd)
                if key not in seen_log_access:
                    alerts.append(
                        f"[LOW] Log File Access | User: {user} | Command: {cmd} | Time: {ts}"
                    )
                    seen_log_access.add(key)

# =========================
# WRITE ALERTS
# =========================
with open(ALERT_FILE, "w") as f:
    for a in alerts:
        f.write(a + "\n")

print(f"[+] Detection complete. Alerts written to {ALERT_FILE}")
