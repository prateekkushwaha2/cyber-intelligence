import dns.resolver
def get_dns_records(domain):

    result = {}

    for record_type in [
        "A",
        "AAAA",
        "MX",
        "NS",
        "TXT"
    ]:

        try:
            answers = dns.resolver.resolve(
                domain,
                record_type
            )

            result[record_type] = [
                str(r)
                for r in answers
            ]

        except:
            result[record_type] = []

    return result