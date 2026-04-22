# Practical 3: ARP Request and Reply Analysis

## Aim

To observe how ARP maps IP addresses to MAC addresses within a local network.

---

## Environment

- System: Laptop with Wireshark  
- Network: Mobile Hotspot  
- OS: Windows  
- Additional Device: Connected to same network  

---

## Procedure

1. Connect both devices to the same network  
2. Clear ARP cache  
3. Start Wireshark capture  
4. Apply filter:

arp


5. Ping the second device  
6. Observe ARP request and reply  

---

## Observations

- ARP request sent as broadcast  
- Only target device responded  
- Reply contained MAC address  
- ARP entries were cached after resolution  

---

## Issues Faced

- No ARP packets initially due to cache  
- Required clearing ARP table  

---

## Analysis

### 1. Broadcast Request
Sender does not know MAC → sends broadcast

### 2. Unicast Reply
Target responds directly with its MAC address

### 3. Layer 2.5 Behavior
ARP operates between:
- Layer 2 (MAC)
- Layer 3 (IP)

---

## Security Perspective

ARP has no authentication, making it vulnerable:

- ARP spoofing  
- Man-in-the-middle attacks  

Indicators of issues:

- Frequent ARP changes  
- Unexpected MAC address mapping  

---

## Conclusion

This practical demonstrated how local network communication begins and highlighted ARP as a critical yet vulnerable protocol in networking.
