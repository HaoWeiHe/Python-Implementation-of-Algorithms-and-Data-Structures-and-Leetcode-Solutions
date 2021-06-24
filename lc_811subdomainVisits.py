class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
google.mail.com: 900
mail.com: 900 + 1
com : 900 + 50 + 1
yahoo.com: 50
intel.mail.com: 1
wiki.org: 1
org: 1
        """
        d = defaultdict(int)
        for ele in cpdomains:
            n, domain = ele.split(" ")
            subd = domain.split(".")
            for idx in range(len(subd)):
                d[".".join(subd[idx:])] += int(n)
        return [ str(d[k])+" " + k for k in d]