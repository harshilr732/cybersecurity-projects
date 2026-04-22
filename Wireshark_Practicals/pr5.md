# Practical 5: ICMP Packet Analysis (Ping Traffic)

## Aim
To analyze ICMP Echo Request and Reply packets and understand their role in connectivity checks and security monitoring.

## Environment
- OS: Windows 10  
- Network: Mobile Hotspot  
- Tool: Wireshark  
- Traffic Generator: Command Prompt  

## Procedure
1. Start capture on Wi-Fi interface  
2. Run:ping 8.8.8.8
3. Stop capture  
4. Apply filter:icmp

## Observations
- Echo Request (Type 8) sent from client  
- Echo Reply (Type 0) received from destination  
- Sequence numbers matched  
- Each request had a corresponding reply  

## Issues Faced
- Mixed traffic initially  
- Filter required to isolate ICMP  

## Analysis
- ICMP is connectionless (no handshake)  
- Used for diagnostics and reachability  
- Request → Reply confirms connectivity  

## Security Perspective
- Used for host discovery (ping sweep)  
- Large volumes may indicate scanning  
- Patterns matter more than single packets  

## Conclusion
ICMP is simple but effective for diagnostics and can also indicate reconnaissance when used in patterns.
