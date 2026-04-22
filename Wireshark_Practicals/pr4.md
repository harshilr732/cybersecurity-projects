# Practical 4: ARP Instability and Duplicate IP (Conceptual)

## Aim

To understand ARP instability caused by duplicate IP addresses and ARP poisoning, and how to differentiate between them.

---

## Core Concept

ARP has no authentication. Any device can claim ownership of an IP address.

This makes the network trust the most recent ARP reply.

---

## Scenario 1: Duplicate IP (Non-Malicious)

### What Happens
- Two devices share the same IP  
- Both respond to ARP requests  

### Observed Behavior
- Multiple ARP replies for the same IP  
- Different MAC addresses in replies  
- Occurs only when a request is made  

### Effect
- Unstable connections  
- Traffic may reach wrong device  
- Session drops  

### Common Causes
- Manual IP misconfiguration  
- DHCP conflicts  
- VM cloning  

---

## Scenario 2: ARP Poisoning (Malicious)

### What Happens
- Attacker sends fake ARP replies  
- Often impersonates the gateway  

### Observed Behavior
- Unsolicited ARP replies  
- Same MAC claiming multiple IPs  
- High frequency of ARP traffic  

### Effect
- Traffic redirected through attacker  
- Possible interception or modification  

---

## Key Differences

| Factor | Duplicate IP | ARP Poisoning |
|-------|-------------|--------------|
| Replies | Only on request | Often unsolicited |
| MAC behavior | Multiple MACs | One MAC for many IPs |
| Frequency | Normal | High |
| Intent | Accidental | Malicious |

---

## Detection (SOC Perspective)

Indicators to monitor:

- Frequent IP–MAC mapping changes  
- ARP replies without requests  
- Gateway MAC address changes  
- Sudden spike in ARP traffic  

---

## Response

Basic mitigation steps:

- Verify anomaly  
- Identify affected systems  
- Check gateway MAC  
- Isolate suspicious device  
- Clear ARP cache if required  

Advanced mitigation:

- Static ARP entries  
- Port security  
- Network monitoring tools  

---

## Conclusion

ARP instability may appear similar in both accidental and malicious scenarios. Correct identification of intent is critical. This practical highlights how small Layer 2 issues can escalate into significant network and security problems.
