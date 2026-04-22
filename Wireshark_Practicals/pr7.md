# Practical 7: TCP Three-Way Handshake Analysis

## Aim
To analyze how TCP establishes a connection using a three-way handshake.

## Environment
- OS: Windows 10  
- Tool: Wireshark  
- Browser: Firefox  

## Procedure
1. Start capture  
2. Visit:http://example.com
3. Stop capture  
4. Apply filter:tcp.flags.syn == 1

## Observations
- SYN → SYN-ACK → ACK sequence observed  
- Connection established successfully  

## Issues Faced
- Background traffic created noise  

## Analysis
- SYN: connection request  
- SYN-ACK: server response  
- ACK: confirmation  

## Security Perspective
- SYN flood attacks exploit incomplete handshakes  
- Indicators:
  - High SYN count  
  - Missing ACK  

## Conclusion
TCP handshake ensures reliable connection establishment and is critical for detecting abnormal traffic patterns.
