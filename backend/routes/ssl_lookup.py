import ssl
import socket
from datetime import datetime

def get_ssl_info(domain):

    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(
                sock,
                server_hostname=domain
            ) as ssock:

                cert = ssock.getpeercert()

        issuer = dict(
            x[0]
            for x in cert["issuer"]
        )

        subject = dict(
            x[0]
            for x in cert["subject"]
        )

        valid_from = cert["notBefore"]
        valid_to = cert["notAfter"]

        expiry_date = datetime.strptime(
            valid_to,
            "%b %d %H:%M:%S %Y %Z"
        )

        days_remaining = (
            expiry_date - datetime.utcnow()
        ).days

        risk = "LOW"

        if days_remaining < 30:
            risk = "HIGH"
        elif days_remaining < 90:
            risk = "MEDIUM"

        return {
            "domain": domain,
            "common_name": subject.get("commonName"),
            "issuer": issuer.get("organizationName"),
            "valid_from": valid_from,
            "valid_until": valid_to,
            "days_remaining": days_remaining,
            "certificate_risk": risk
        }

    except Exception as e:
        return {
            "error": str(e)
        }