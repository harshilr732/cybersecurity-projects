import json

# Tier-2 Investigation Function
def tier2_investigation(alert):
    text = alert["email_preview"].lower()

    # Credential phishing
    cred_terms = ["password", "login", "verify", "account suspended"]
    if any(t in text for t in cred_terms):
        return "True Positive - Credential Phishing"

    # Pharma scam
    pharma_terms = ["viagra", "cialis", "xanax", "valium"]
    if any(t in text for t in pharma_terms):
        return "True Positive - Pharma Scam"

    # Spam campaign
    spam_terms = ["free", "coupon", "gift", "vacation", "hotel", "save", "deal"]
    if any(t in text for t in spam_terms):
        return "True Positive - Spam Campaign"

    # Legit safe emails
    safe_terms = ["invoice", "receipt", "order confirmation"]
    if any(t in text for t in safe_terms):
        return "False Positive - Legit Business"

    return "Needs Manual Review"


# Response Playbook Function
def response_playbook(alert, decision):
    if "Spam Campaign" in decision:
        return {
            "action": "Quarantine Email",
            "containment": "Add sender/domain to blocklist",
            "priority": "Medium"
        }

    if "Credential Phishing" in decision:
        return {
            "action": "Immediate Escalation",
            "containment": "Block domain + Notify user",
            "priority": "High"
        }

    if "Manual Review" in decision:
        return {
            "action": "Create Analyst Ticket",
            "containment": "Pending investigation",
            "priority": "Low"
        }

    return {
        "action": "No Action",
        "containment": "N/A",
        "priority": "Info"
    }


# Load alerts
with open("alerts.json", "r") as f:
    alerts = json.load(f)

# Apply Tier-2 + Response
for a in alerts[:10]:
    decision = tier2_investigation(a)
    response = response_playbook(a, decision)

    print("\nAlert:", a["alert_id"])
    print("Decision:", decision)
    print("Response Action:", response)

    import json
from datetime import datetime

# Load alerts
with open("alerts.json", "r") as f:
    alerts = json.load(f)

incident_tickets = []

case_id = 1

for alert in alerts[:50]:  # start with first 20 alerts
    decision = tier2_investigation(alert)
    response = response_playbook(alert, decision)

    ticket = {
        "case_id": f"CASE-{case_id:04d}",
        "created_time": str(datetime.now()),
        "alert_id": alert["alert_id"],
        "severity": alert["severity"],
        "tier2_verdict": decision,
        "response_action": response["action"],
        "priority": response["priority"],
        "status": "Open" if "Manual Review" in decision else "Contained",
        "notes": "Auto-generated SOC case from phishing/spam pipeline"
    }

    incident_tickets.append(ticket)
    case_id += 1

# Save tickets
with open("incident_cases.json", "w") as f:
    json.dump(incident_tickets, f, indent=4)

print("Generated Incident Tickets:", len(incident_tickets))
print("Saved to incident_cases.json")

# Show one example ticket
print("\nExample Ticket:\n", incident_tickets[0])
