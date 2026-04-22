# Practical 9: DNS Traffic Analysis (UDP)

## Aim
To analyze DNS queries and responses over UDP.

## Procedure
1. Start capture  
2. Visit a website  
3. Apply filter:dns

## Observations
- Queries sent to port 53  
- Responses contained IP addresses  
- No handshake observed  

## Analysis
- DNS uses UDP for speed  
- Stateless communication  

## Security Perspective
- DNS can be abused for:
  - Amplification attacks  
  - Tunneling  
  - C2 communication  

## Conclusion
DNS is fast and efficient but vulnerable due to lack of connection validation.
