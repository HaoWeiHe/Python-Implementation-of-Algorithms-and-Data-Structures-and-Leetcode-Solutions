class Solution(object):
    def accountsMerge(self, accounts):
        """
        1   a
        2   b
        3   c 
            d
        """
        #account = id -> mail
        #setup reverse direction graph
        allmail = set()
        visted = set()
        mail2idx = collections.defaultdict(set)
        for idx, a in enumerate(accounts):
            name, mails = a[0], a[1:]
            for m in mails:
                allmail.add(m)
                mail2idx[m].add(idx)
        res =[]
        for mail in allmail:
            if mail in visted:
                continue
            tmp = []
            q = deque([mail])
            while q:
                top = q.popleft() #mail
                if top in visted:
                    continue
                tmp.append(top)
                for idx in mail2idx[top]:
                    name, explore = accounts[idx][0], accounts[idx][1:]
                    for new in explore:
                        if new not in visted:
                            q.append(new)
                visted.add(top)
            res.append([name] + sorted(tmp))
        return res
                        