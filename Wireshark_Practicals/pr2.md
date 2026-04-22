# Practical 2: Understanding Packet Structure and OSI Layers

## Aim

To understand how a network packet is structured, how protocol headers are layered, and how they relate to the OSI model.

---

## Environment

- Tool: Wireshark  
- Interface: Wi-Fi  
- Packet Type: TCP (TLS traffic)  

---

## Procedure

1. Open Wireshark and start capture on Wi-Fi interface  
2. Visit `https://example.com`  
3. Stop capture after page load  
4. Apply filter:
tls.handshake.type == 1

5. Select a TLS Client Hello packet  
6. Expand all protocol layers  

---

## Observations

A TLS 1.3 Client Hello packet was identified with multiple protocol layers:

### 1. Frame (Capture Layer)
- Frame number and size (~499 bytes)  
- Timestamp and interface details  
- Metadata added during capture  

### 2. Ethernet II (Layer 2 – Data Link)
- Source MAC  
- Destination MAC  
- Type: IPv6  

### 3. IPv6 (Layer 3 – Network)
- Source and destination IP  
- Payload length  
- Next header: TCP  

### 4. TCP (Layer 4 – Transport)
- Source port  
- Destination port: 443  
- Sequence and acknowledgment numbers  

### 5. TLS 1.3 (Application Layer)
- Handshake: Client Hello  
- SNI: example.com  

---

## Key Concept: Encapsulation

Each layer adds its own header before transmission.  
At the receiver, headers are removed step-by-step (decapsulation).

---

## Issues Faced

- Mapping Wireshark layers to OSI model was initially confusing  
- Some fields required deeper inspection  

---

## Analysis

A single packet contains multiple layers:

- Lower layers → delivery  
- Transport layer → reliability  
- Application layer → secure communication  

---

## Security Perspective

Understanding packet structure helps identify:

- Malformed packets  
- Suspicious TCP behavior  
- Spoofed IP or MAC addresses  
- Protocol misuse  

---

## Conclusion

This practical clarified how packets are structured across layers and how Wireshark represents them. It strengthens understanding of real-world network communication.
