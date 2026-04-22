import pandas as pd

# Load dataset
df = pd.read_csv("phishing_email.csv")

# Filter phishing emails
phish_df = df[df["label"] == 1]

# Common phishing keywords
phishing_keywords = [
    "urgent", "verify", "password", "account",
    "login", "click", "bank", "security",
    "confirm", "update", "suspended"
]

# Check first 5 phishing emails
for i in range(5):
    text = str(phish_df["text_combined"].iloc[i]).lower()

    matched = [word for word in phishing_keywords if word in text]

    print("\n--- Phishing Email", i+1, "---")
    print("Matched Keywords:", matched)
    print("Text Preview:", text[:200])
