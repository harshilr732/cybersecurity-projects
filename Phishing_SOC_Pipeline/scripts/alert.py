import pandas as pd
import json
from datetime import datetime

df = pd.read_csv("phishing_email.csv")

suspicious_terms = [
    "click", "offer", "free", "discount",
    "money back", "no prescription",
    "viagra", "cialis", "xanax",
    "weight loss", "guarantee"
]

safe_terms = [
    "order confirmation",
    "registration confirmation",
    "invoice",
    "receipt",
    "newsletter"
]

def detect_terms(text):
    text = str(text).lower()
    matched = [t for t in suspicious_terms if t in text]
    safe = [s for s in safe_terms if s in text]
    return matched, safe

def score_email(text):
    matched, safe = detect_terms(text)
    score = len(matched)*10 - len(safe)*20
    return score, matched

alerts = []

for idx, row in df.iterrows():
    score, matched = score_email(row["text_combined"])

    if score >= 30:
        alert = {
            "alert_id": f"PHISH-{idx}",
            "timestamp": str(datetime.now()),
            "risk_score": score,
            "severity": "High" if score >= 50 else "Medium",
            "matched_indicators": matched,
            "email_preview": row["text_combined"][:120],
            "true_label": int(row["label"])
        }
        alerts.append(alert)

# Save alerts to JSON file
with open("alerts.json", "w") as f:
   json.dump(alerts, f, indent=4)

print("Generated alerts:", len(alerts))
print("Saved sample alerts to alerts.json")
print("\nExample Alert:\n", alerts[0])
