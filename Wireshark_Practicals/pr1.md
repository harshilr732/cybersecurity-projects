# Practical 1: Interface Selection and Basic Traffic Capture

## Aim

To identify the correct network interface, capture live traffic, and analyze HTTPS and ICMP activity.

---

## Environment

- OS: Windows 10  
- Network: Mobile Hotspot  
- Tool: Wireshark  
- Browser: Firefox  

---

## Procedure

### Part A: HTTPS Traffic

1. Start Wireshark capture on Wi-Fi interface  
2. Open browser and visit `www.example.com`  
3. Apply filter: tls.handshake.type == 1
4. Identify TLS Client Hello  

---

### Part B: ICMP Traffic

1. Start new capture  
2. Run:ping www.google.com
3. Apply filter: icmpv6

---

## Observations

- Background traffic present even before user action  
- DNS queries occur before connection  
- TLS Client Hello reveals domain via SNI  
- ICMP request–reply confirms connectivity  

---

## Analysis

- Modern systems generate continuous background traffic  
- TLS handshake exposes metadata before encryption  
- IPv6 preferred over IPv4 in modern networks  

---

## Security Perspective

- ICMP used for host discovery and scanning  
- Repeated ping patterns may indicate reconnaissance  

---

## Conclusion

This practical demonstrates how to capture and filter traffic, and highlights that network analysis often relies on metadata due to encryption.
