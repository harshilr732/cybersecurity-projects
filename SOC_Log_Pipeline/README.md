# Log-Based SOC Detection & Incident Analysis Pipeline

This project implements a lightweight Security Operations Center (SOC) pipeline that ingests Linux system logs, applies rule-based detection, correlates security events, and generates a structured incident report.

The goal is to simulate real SOC analyst workflows without relying on heavy SIEM platforms.

---

## Overview

The pipeline processes authentication logs and system logs to detect suspicious activities such as:

- SSH brute force attacks  
- Successful login after multiple failures  
- Sensitive file access (`/etc/shadow`, `/etc/passwd`)  
- Unauthorized service modifications  
- Execution of scripts from temporary directories  

The system produces a consolidated incident report highlighting potential attack patterns.

---

## Pipeline Flow

Log Generation (Ubuntu VM)
        ->
Log Normalization (Python)
        ->
Detection Engine (Rule-Based)
        ->
Correlation Logic
        ->
Alert Files (Auth + Syslog)
        ->
Final Incident Report


---

## Components

### 1. Log Generation
- Auth logs and syslogs generated in an Ubuntu VM  
- Simulated attack scenarios (SSH brute force, privilege escalation, persistence)

### 2. Log Normalization
- Raw logs converted into structured CSV format  
- Extracted fields:
  - Timestamp  
  - Username  
  - Source IP  
  - Event type  
  - Command  

### 3. Detection Engine

Python scripts analyze normalized logs using rule-based detection.

#### Auth Log Detection:
- SSH brute force (time-based threshold)  
- Successful login after multiple failures  
- Sensitive file access (`/etc/shadow`, `/etc/passwd`)  
- SSH service modification (persistence technique)  
- Log access activity (deduplicated)

#### Syslog Detection:
- Script execution from `/tmp` and `/dev/shm`  
- Suspicious download and execution patterns  
- Netcat usage indicators  

---

## Correlation Logic

The system correlates multiple events to identify attack progression:

- Brute force → Successful login → Account compromise  
- Compromise → Sensitive file access  
- Post-compromise → Execution from temporary directory  

High-confidence alert generated:



---

## Output

The system generates:

- `auth_alerts.txt` → Authentication-based alerts  
- `syslog_alerts.txt` → System-level alerts  
- `final_report.txt` → Consolidated incident report  

---

## Sample Incident Summary

Multi-stage intrusion pattern detected:

- Brute force activity observed  
- Possible credential compromise  
- Sensitive file access detected  
- Execution from temporary directory (possible payload execution)  

---

## Example Attack Flow

- SSH brute force detected from attacker IP  
- Successful login after repeated failures  
- Sensitive file `/etc/shadow` accessed  
- Script executed from `/tmp` via cron job  

This demonstrates a realistic multi-stage attack scenario.

---

## How to Run

Run the scripts in order:

```bash
python detect_auth_alerts.py
python detect_sys_alerts.py
python final_report.py
```

Output will be generated in:

- final_report.txt
### Technologies Used
- Python
- Linux (Ubuntu VM)
- Log analysis techniques
- Rule-based detection
### Limitations
- Rule-based detection only (no ML or behavioral baselining)
- No real-time monitoring (offline analysis)
- Limited log sources (auth + syslog only)
### Future Improvements
- Integration with lightweight SIEM (Wazuh / ELK)
- Real-time log ingestion
- Advanced correlation engine
- Visualization dashboard
### Purpose
This project demonstrates foundational SOC skills including:
- Log analysis
- Threat detection
- Event correlation
- Incident reporting
