# Networking Labs using Cisco Packet Tracer

## Overview

This repository contains a structured set of 12 networking practicals implemented using Cisco Packet Tracer. The labs cover core networking concepts from Layer 2 switching to Layer 3 routing, and extend into security-focused topics such as VLAN segmentation, ACLs, NAT, DHCP, DNS, and lateral movement prevention.

Each practical includes:

* Network topology design
* Step-by-step configuration
* Verification commands
* Troubleshooting guidance
* Security/SOC relevance

These labs are designed to build both **networking fundamentals** and **security analysis skills** required for SOC roles.

---

## Lab List

### Basic Networking

1. **Basic IP Addressing and Subnetting**
   File: `practical-1-ip-addressing.txt`

2. **Switch Fundamentals (MAC Learning & Flooding)**
   File: `practical-2-switch-fundamentals.txt`

3. **ARP Behavior and Troubleshooting**
   File: `practical-3-arp-behavior.txt`

---

### VLANs and Segmentation

4. **VLAN Creation and Port Assignment**
   File: `practical-4-vlan-configuration.txt`

5. **VLAN Trunking (802.1Q) and Allowed VLANs**
   File: `practical-5-vlan-trunking-8021q.txt`

6. **Inter-VLAN Routing (Router-on-a-Stick)**
   File: `practical-6-inter-vlan-routing-router-on-a-stick.txt`

---

### Network Security Controls

7. **ACLs for Inter-VLAN Access Control**
   File: `practical-7-acl-inter-vlan-access-control.txt`

8. **NAT (Inside vs Outside) with Overload**
   File: `practical-8-nat-inside-outside-overload.txt`

9. **DHCP Server and DHCP Relay**
   File: `practical-9-dhcp-server-relay.txt`

10. **DNS Basics (Name Resolution)**
    File: `practical-10-dns-basics-name-resolution.txt`

---

### Security Simulation & Defense

11. **Firewall Rules using ACLs (Traffic Filtering)**
    File: `practical-11-firewall-rules-acl-filtering.txt`

12. **Network Segmentation Attack Simulation (Lateral Movement)**
    File: `practical-12-network-segmentation-lateral-movement.txt`

---

## Tools Used

* Cisco Packet Tracer
* Basic CLI (Cisco IOS)
* Networking Protocols: ARP, VLAN, DHCP, DNS, NAT, ICMP, TCP

---

## Key Concepts Covered

* IP Addressing and Subnetting
* Layer 2 Switching (MAC Table, Flooding)
* VLAN Segmentation and Trunking
* Inter-VLAN Routing
* Access Control Lists (ACLs)
* Network Address Translation (NAT)
* Dynamic Host Configuration Protocol (DHCP)
* Domain Name System (DNS)
* Firewall Filtering
* Lateral Movement Detection and Prevention

---

## Security Perspective (SOC Focus)

These labs are designed with a security mindset:

* Understanding internal vs external traffic
* Detecting lateral movement patterns
* Interpreting ACL and firewall behavior
* Mapping NAT translations during investigations
* Identifying ARP/DHCP-based attacks
* Observing segmentation failures

---

## How to Use This Repository

1. Open each practical `.txt` file
2. Recreate the topology in Cisco Packet Tracer
3. Follow configuration steps
4. Verify using given commands
5. Capture outputs/screenshots for practice

---

## Outcome

After completing all labs, you will have:

* Strong foundation in networking fundamentals
* Practical experience with Cisco CLI
* Understanding of real-world network security controls
* SOC-relevant troubleshooting and analysis skills

---
