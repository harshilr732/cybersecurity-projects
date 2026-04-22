import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="SOC Phishing Dashboard", layout="wide")

st.title("📌 SOC Phishing & Spam Detection Dashboard")

# Load alerts
with open("alerts.json", "r") as f:
    alerts = json.load(f)

# Load incident tickets
with open("incident_cases.json", "r") as f:
    tickets = json.load(f)

# Convert to DataFrames
alerts_df = pd.DataFrame(alerts)
tickets_df = pd.DataFrame(tickets)

# Summary Metrics
st.subheader("SOC Overview Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Alerts", len(alerts_df))
col2.metric("Total Incident Cases", len(tickets_df))
col3.metric("High Severity Alerts", len(alerts_df[alerts_df["severity"] == "High"]))

# Alert Filtering
st.subheader("Alert Viewer (Tier-1 Output)")

severity_filter = st.selectbox(
    "Filter by Severity",
    options=["All", "Medium", "High"]
)

if severity_filter != "All":
    filtered_alerts = alerts_df[alerts_df["severity"] == severity_filter]
else:
    filtered_alerts = alerts_df

st.dataframe(filtered_alerts[[
    "alert_id", "severity", "risk_score",
    "matched_indicators", "email_preview"
]])

# Incident Ticket Viewer
st.subheader("Incident Case Management (Tier-2 + Response)")

st.dataframe(tickets_df[[
    "case_id", "alert_id", "tier2_verdict",
    "response_action", "priority", "status"
]])


st.subheader("Case Drill-Down View")

# Select a case
selected_case = st.selectbox(
    "Select Case ID to View Details",
    tickets_df["case_id"].tolist()
)

case_details = tickets_df[tickets_df["case_id"] == selected_case].iloc[0]

st.write("### Case Details")
st.json(case_details.to_dict())
