import requests

def analyze_headers(domain):

    try:
        url = f"https://{domain}"

        response = requests.get(
            url,
            timeout=10
        )

        headers = response.headers

        checks = {
            "Content-Security-Policy":
                headers.get("Content-Security-Policy"),

            "Strict-Transport-Security":
                headers.get("Strict-Transport-Security"),

            "X-Frame-Options":
                headers.get("X-Frame-Options"),

            "X-Content-Type-Options":
                headers.get("X-Content-Type-Options"),

            "Referrer-Policy":
                headers.get("Referrer-Policy")
        }

        score = 100

        issues = []

        for key, value in checks.items():

            if not value:
                score -= 20
                issues.append(
                    f"Missing {key}"
                )

        return {
            "score": max(score, 0),
            "headers": checks,
            "issues": issues
        }

    except Exception as e:
        return {
            "error": str(e)
        }