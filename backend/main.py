from fastapi import FastAPI
from routes.ssl_lookup import get_ssl_info
import time
from routes.dns import get_dns_records
from routes.whois_lookup import get_whois_info
from routes.headers_lookup import analyze_headers
from routes.risk_engine import calculate_risk


app = FastAPI()


@app.get("/")
def home():
    return {"message":"Cyber Intelligence API"}

@app.get("/ssl/{domain}")
def ssl_lookup(domain:str):
    return get_ssl_info(domain)

@app.get("/dns/{domain}")
def dns_lookup(domain:str):
    return get_dns_records(domain)

@app.get("/whois/{domain}")
def whois_lookup(domain:str):
    return get_whois_info(domain)

@app.get("/headers/{domain}")
def headers_scan(domain: str):
    return analyze_headers(domain)

@app.get("/intelligence/{domain}")
def intelligence(domain: str):

    start = time.time()

    dns_data = get_dns_records(domain)
    whois_data = get_whois_info(domain)
    ssl_data = get_ssl_info(domain)
    headers_data = analyze_headers(domain)
    risk_data = calculate_risk(
    ssl_data,
    headers_data
)

    elapsed = round(time.time() - start, 2)

    return {
        "domain": domain,
        "scan_time_seconds": elapsed,
        "dns": dns_data,
        "whois": whois_data,
        "ssl": ssl_data,
        "headers": headers_data,
        "risk": risk_data
    }