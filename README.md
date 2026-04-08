#  ScamShield-OpenEnv 🛡️

##  Overview

ScamShield-OpenEnv is a real-world reinforcement learning (RL) environment designed to train and evaluate AI agents for scam detection and safe decision-making.

The environment simulates realistic scam scenarios such as OTP fraud, UPI scams, phishing links, job scams, and social engineering attacks.

---

##  Motivation

Online scams are rapidly increasing, especially in India.

Common threats include:
- OTP fraud
- UPI scams
- Fake job offers
- Impersonation attacks
- Phishing links

This project enables AI systems to detect scams and recommend safe actions.

---

##  Environment Design

### Observation Space

Each observation includes:
- `message`: text content
- `metadata`: sender, platform, urgency
- `history`: previous actions

---

### Action Space

The agent can take the following actions:
- `scam`
- `legit`
- `report`
- `block`
- `warn_user`
- `verify_contact`
- `ignore`

---

### Reward Function

The reward is calculated as:

- Correct classification → +0.4  
- Reasoning quality → +0.2  
- Safe action → +0.3  
- Risk awareness → +0.1  
- Dangerous advice → penalty  

All rewards are between **0.0 and 1.0** and deterministic.

---

##  Real-World Impact Simulation

The environment simulates consequences:

- Unsafe action → possible financial loss  
- Safe action → user protection  

---

##  Tasks

| Task | Description | Difficulty |
|------|------------|-----------|
| basic_detection | classify scam | Easy |
| contextual_analysis | explain reasoning | Medium |
| full_defense | detect and act safely | Hard |

---

##  Key Features

- Real Indian scam scenarios (OTP, UPI, job fraud)
- Social engineering detection
- Multi-action decision system
- Safety-first reward design
- Deterministic evaluation

---

##  Setup Instructions

Install dependencies:

```bash
pip install -r requirements.txt


This mimics real human decision-making and improves reliability.

---

## Tasks

| Task | Description | Difficulty |
|------|------------|-----------|
| basic_detection | Identify scam messages | Easy |
| contextual_analysis | Analyze reasoning | Medium |
| full_defense | Detect and take safe action | Hard |

---

## Dataset

The dataset includes realistic scenarios such as:

- OTP and banking fraud  
- UPI scams  
- Fake urgency messages  
- Known contact impersonation  
- Legitimate everyday messages  

It is designed to reflect real-world communication patterns.

---

## Key Features

- Real-world scam scenarios (India-focused)
- Context-aware decision making
- Multi-step reasoning
- Safety-driven reward system
- Deterministic evaluation
- Docker-compatible execution

---

## Setup Instructions

Install dependencies:

```bash
pip install -r requirements.txt