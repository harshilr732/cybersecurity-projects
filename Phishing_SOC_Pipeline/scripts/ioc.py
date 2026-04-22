import pandas as pd
import re

# Load dataset
df = pd.read_csv("phishing_email.csv")

# Filter only phishing emails
phish_df = df[df["label"] == 1]

print("Total phishing emails:", len(phish_df))

# Function to extract URLs
def extract_urls(text):
    url_pattern = r"http[s]?://\S+|www\.\S+"
    return re.findall(url_pattern, str(text))

# Test on first 5 phishing emails
for i in range(5):
    email_text = phish_df["text_combined"].iloc[i]
    urls = extract_urls(email_text)

    print ("\n--- Phishing Email", i+1, "---")
    print("Extracted URLs:", urls)
