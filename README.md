# Phishing URL Detection System (Rule-Based + ML)

## Overview
This project presents a phishing URL detection system developed for academic demonstration.
The system classifies URLs as **Phishing** or **Legitimate** using two approaches:
1. Rule-Based Detection (default)
2. Machine Learning–Based Detection (experimental)
<img width="1430" height="803" alt="image" src="https://github.com/user-attachments/assets/4c6b8d23-40c3-42e7-b484-9a75be8ea43d" />

   

The objective is to study URL-based phishing characteristics and understand the strengths
and limitations of heuristic and ML-based detection.

## Why this project exists
Phishing attacks frequently rely on deceptive URLs.
This project demonstrates how URLs can be analyzed using:
- Structural patterns
- Textual features
- Supervised machine learning models

## What this project IS
- A URL-based phishing classification system
- A comparison of rule-based and ML-based detection
- An academic prototype aligned with UCI phishing datasets
- A controlled demo system for understanding phishing behavior

## What this project is NOT
- ❌ Not a browser security engine (Chrome / Safe Browsing)
- ❌ Not a real-time DNS or WHOIS system
- ❌ Not an SSL certificate or reputation checker
- ❌ Not a live web crawler or threat intelligence system

## Modes of Operation

### Rule-Based Mode (Default)
<img width="1434" height="781" alt="image" src="https://github.com/user-attachments/assets/639c084d-87f1-4065-a128-ffa15d1e671b" />

Uses predefined heuristic rules such as:
- URL length
- Presence of suspicious keywords
- Use of IP addresses
- Excessive special characters
- Domain structure patterns

This mode is deterministic, explainable, and suitable for academic evaluation.

### ML-Based Mode (Experimental)
Uses a supervised machine learning model trained on the
**UCI Phishing Website Dataset (~11,000 URLs)**.

⚠️ This mode is intentionally strict and may classify legitimate URLs as phishing
due to limited contextual information.
<img width="1434" height="716" alt="image" src="https://github.com/user-attachments/assets/0529578b-97a0-4995-8843-2f927f74acf9" />


## Why ML Mode Is Strict
The ML model operates only on static URL features.
It does not include:
- Live DNS reputation
- SSL certificate validation
- Historical domain behavior
- Web content analysis

<img width="1618" height="763" alt="image" src="https://github.com/user-attachments/assets/d64cdc40-a78f-4024-9959-37a634045857" />


As a result, the model may produce false positives, which is discussed as a limitation.

## Dataset
- Source: UCI Phishing Website Dataset
- Format: ARFF
- Labels:
  - 1 → Legitimate
  - -1 → Phishing

## Technologies Used
- Python
- Flask
- Pandas
- Scikit-learn
- HTML & CSS

## Academic Disclaimer
This project is developed strictly for academic learning and demonstration purposes.
