def calculate_risk(ssl_data, headers_data):

    score = 100
    findings = []

    if ssl_data.get("certificate_risk") == "HIGH":
        score -= 30
        findings.append("SSL certificate expires soon")

    elif ssl_data.get("certificate_risk") == "MEDIUM":
        score -= 15
        findings.append("SSL certificate should be renewed")

    for issue in headers_data.get("issues", []):
        findings.append(issue)

    score -= len(headers_data.get("issues", [])) * 10

    score = max(score, 0)

    if score >= 80:
        risk_level = "LOW"

    elif score >= 50:
        risk_level = "MEDIUM"

    else:
        risk_level = "HIGH"

    return {
        "security_score": score,
        "risk_level": risk_level,
        "findings": findings
    }