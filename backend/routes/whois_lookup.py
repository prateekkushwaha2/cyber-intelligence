import whois

def safe_value(value):

    if isinstance(value, list):
        return str(value[0])

    return str(value)

def get_whois_info(domain):

    try:
        data = whois.whois(domain)

        return {
            "domain": domain,
            "registrar": safe_value(data.registrar),
            "creation_date": safe_value(data.creation_date),
            "expiration_date": safe_value(data.expiration_date),
            "updated_date": safe_value(data.updated_date),
            "name_servers": data.name_servers
        }

    except Exception as e:
        return {"error": str(e)}