# Practical 6: Traceroute and TTL Analysis

## Aim
To understand how traceroute works using TTL and ICMP Time Exceeded messages.

## Environment
- OS: Windows 10  
- Tool: Wireshark  
- Command: tracert  

## Procedure
1. Start capture  
2. Run:tracert 8.8.8.8
3. Stop capture  
4. Apply filter:icmp

## Observations
- TTL increased step-by-step  
- Intermediate routers returned:
  - Type 11 (Time Exceeded)  
- Some hops did not respond  
- Final destination sent Echo Reply  

## Issues Faced
- Missing hops due to filtering or rate limiting  

## Analysis
- TTL limits packet lifetime  
- Each hop decrements TTL  
- When TTL = 0 → router sends ICMP Time Exceeded  

## Security Perspective
- Reveals network path  
- Useful for reconnaissance  
- Repeated probing may indicate scanning  

## Conclusion
Traceroute exposes network paths and demonstrates TTL behavior in routing.
