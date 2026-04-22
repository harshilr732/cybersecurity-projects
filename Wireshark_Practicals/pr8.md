# Practical 8: TCP Connection Termination (FIN vs RST)

## Aim
To differentiate between normal and abnormal TCP connection termination.

## Procedure
1. Start capture  
2. Open and close a website  
3. Apply filter:tcp.flags.fin == 1 || tcp.flags.reset == 1

## Observations
- FIN → ACK → FIN → ACK (normal)  
- RST observed in some cases  

## Analysis
- FIN = graceful termination  
- RST = immediate termination  

## Security Perspective
- Frequent RST may indicate:
  - Errors  
  - Blocking  
  - Scanning  

## Conclusion
FIN is normal termination; RST indicates abrupt closure and may require analysis.
