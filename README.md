# cyber intelligence Platform

# Cyber Intelligence API

A lightweight **Cyber Intelligence API** built with **FastAPI** that performs domain reconnaissance and security analysis.

This API provides:

* SSL Certificate Lookup
* DNS Record Analysis
* WHOIS Information Lookup
* Security Header Inspection
* Risk Scoring Engine
* Combined Intelligence Scan

---

## Features

### SSL Lookup

Retrieve SSL certificate information for a domain.

**Endpoint**

```http
GET /ssl/{domain}
```

Example:

```http
GET /ssl/google.com
```

---

### DNS Lookup

Fetch DNS records for a domain.

**Endpoint**

```http
GET /dns/{domain}
```

Example:

```http
GET /dns/google.com
```

---

### WHOIS Lookup

Retrieve domain registration information.

**Endpoint**

```http
GET /whois/{domain}
```

Example:

```http
GET /whois/google.com
```

---

### Header Analysis

Analyze HTTP response headers and identify security configurations.

**Endpoint**

```http
GET /headers/{domain}
```

Example:

```http
GET /headers/google.com
```

---

### Full Intelligence Scan

Run all scans together and generate a risk assessment.

**Endpoint**

```http
GET /intelligence/{domain}
```

Example:

```http
GET /intelligence/google.com
```

Example Response:

```json
{
  "domain": "google.com",
  "scan_time_seconds": 1.42,
  "dns": {},
  "whois": {},
  "ssl": {},
  "headers": {},
  "risk": {}
}
```

---

# Installation (Kali Linux)

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace:

* `YOUR_USERNAME`
* `YOUR_REPOSITORY`

with your actual GitHub repository details.

---

## 2. Update Packages

```bash
sudo apt update
```

---

## 3. Install Python

```bash
sudo apt install python3 python3-pip python3-venv -y
```

Verify installation:

```bash
python3 --version
pip3 --version
```

---

## 4. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Expected:

```text
(venv)
```

---

## 5. Install Dependencies

If `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

Otherwise:

```bash
pip install fastapi uvicorn python-whois dnspython requests
```

Generate requirements later:

```bash
pip freeze > requirements.txt
```

---

## 6. Run the API

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Expected:

```text
INFO: Uvicorn running on http://0.0.0.0:8000
```

---

# Usage

Open:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# API Examples

SSL:

```bash
curl http://127.0.0.1:8000/ssl/example.com
```

DNS:

```bash
curl http://127.0.0.1:8000/dns/example.com
```

WHOIS:

```bash
curl http://127.0.0.1:8000/whois/example.com
```

Headers:

```bash
curl http://127.0.0.1:8000/headers/example.com
```

Full Intelligence:

```bash
curl http://127.0.0.1:8000/intelligence/example.com
```

---

# Project Structure

```text
.
├── main.py
├── requirements.txt
├── routes/
│   ├── ssl_lookup.py
│   ├── dns.py
│   ├── whois_lookup.py
│   ├── headers_lookup.py
│   └── risk_engine.py
└── README.md
```

---

# Stop Server

```text
CTRL + C
```

---

# Disclaimer

This project is intended for:

* Security learning
* Domain analysis
* Defensive research
* Educational use

Only scan domains and systems you are authorized to inspect.

---

# License

MIT License

