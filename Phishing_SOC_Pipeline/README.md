# Phishing Detection & SOC Incident Response Pipeline

This project simulates a Security Operations Center (SOC) workflow for detecting and investigating phishing emails using rule-based analysis and case management.

---

## Objective

To detect phishing emails, generate alerts, investigate incidents, and produce structured SOC reports.

---

## Workflow
Email Dataset
->
Keyword Analysis & Scoring
->
Alert Generation
->
Incident Case Creation
->
Investigation (IOC Analysis)
->
Report Generation

---

## Components

### 1. Keyword Analysis
- Detects phishing patterns using keywords
- Identifies urgency, credential requests, and financial fraud indicators

### 2. Scoring System
- Assigns risk score to emails based on suspicious indicators

### 3. Alert Generation
- Flags high-risk emails
- Stores alerts in JSON format

### 4. Incident Management
- Creates structured incident cases
- Tracks phishing investigations

### 5. Investigation
- Extracts Indicators of Compromise (IOCs)
- Analyzes attacker behavior

### 6. Report Generation
- Produces SOC-style incident reports

---

## Dataset

- Phishing email dataset (CSV format)
- Contains labeled email data for analysis

---

## Output

- `alerts.json` → detected phishing alerts  
- `incident_cases.json` → structured cases  
- `case_report_1.txt` → detailed investigation report  
- `summary_report.txt` → overall analysis summary  

---

## How to Run

```bash
python keyword_analysis.py
python score.py
python alert.py
python investigation.py
python report_generator.py
```
### Technologies Used
- Python
- Pandas
- JSON processing
- Rule-based detection
### Limitations
- Keyword-based detection (no ML/NLP)
- Dependent on dataset quality
- Limited automation
### Future Improvements
- Machine learning-based phishing detection
- NLP for email content analysis
- URL reputation analysis
- Real-time email monitoring
### Purpose
This project demonstrates:

- Phishing detection techniques
- SOC alerting and case management
- Incident investigation workflow
- Report generation
