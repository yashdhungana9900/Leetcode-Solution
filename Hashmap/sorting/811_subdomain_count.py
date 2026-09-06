class Solution(object):
    def subdomainVisits(self, cpdomains):
        count = {}

        for item in cpdomains:
            visits, domain = item.split()
            visits = int(visits)

            parts = domain.split(".")

            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                count[subdomain] = count.get(subdomain, 0) + visits

        result = []

        for domain in count:
            result.append(str(count[domain]) + " " + domain)

        return result