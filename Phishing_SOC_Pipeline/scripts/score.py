import pandas as pd

df = pd.read_csv("phishing_email.csv")

suspicious_terms = [
    "click", "offer", "free", "discount",
    "money back", "no prescription",
    "viagra", "cialis", "xanax",
    "weight loss", "guarantee"
]

# Whitelist terms (legitimate business context)
safe_terms = [
    "order confirmation",
    "registration confirmation",
    "invoice",
    "receipt",
    "newsletter"
]

def score_email(text):
    text = str(text).lower()
    score = 0

    # Add suspicious scoring
    for term in suspicious_terms:
        if term in text:
            score += 10

    # Reduce score if safe context found
    for safe in safe_terms:
        if safe in text:
            score -= 20

    return score

df["risk_score"] = df["text_combined"].apply(score_email)
df["alert"] = df["risk_score"] >= 30

alerts = df[df["alert"] == True]

print("Total alerts after tuning:", len(alerts))
print("\nAlert breakdown:")
print(alerts["label"].value_counts())

precision = len(alerts[alerts["label"] == 1]) / len(alerts)
print("\nNew Precision:", precision)
