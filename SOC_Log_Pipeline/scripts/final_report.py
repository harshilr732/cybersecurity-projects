OUTPUT = "final_report.txt"

auth_content = open("auth_alerts.txt").read()
sys_content = open("syslog_alerts.txt").read()

with open(OUTPUT, "w") as out:
    out.write("===== AUTH ALERTS =====\n\n")
    out.write(auth_content)

    out.write("\n===== SYSLOG ALERTS =====\n\n")
    out.write(sys_content)

    out.write("\n===== INCIDENT SUMMARY =====\n\n")

    if "SSH Brute Force" in auth_content and "Sensitive File Access" in auth_content:
        out.write("Multi-stage intrusion pattern detected:\n")
        out.write("- Brute force activity observed\n")
        out.write("- Possible credential compromise\n")
        out.write("- Sensitive file access detected\n")

    if "/tmp" in sys_content:
        out.write("- Execution from temporary directory (possible payload execution)\n")

print(f"[+] Final report generated: {OUTPUT}")
