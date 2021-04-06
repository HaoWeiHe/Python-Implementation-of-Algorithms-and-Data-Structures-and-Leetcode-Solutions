class Solution(object):
    def accountsMerge(self, accounts):
        """
[["John","A","B"],["John","C","B"],

["Mary","Z"]

G1: acc1 acc2, 
G2: acc3 acc4

        graph = {A: [acc1], B:[acc1,acc2], C: [acc2,acc8], Z:[acc3],  } 
        accs = {acc1:[A,B], acc2:[B,C] }
        allmails : [A, B,C,D]
        
        acc1: check [A,B,C] #tmp : [acc1, acc1, acc2,acc2, acc8] visted:AB 
        
        #bfs
        """
        allmails = set()
        group = defaultdict(list)
        for i,e in enumerate(accounts):
            for mail in e[1:]:
                group[mail].append(i)
                allmails.add(mail)
          
        visted = set()
        res  = []
        for mail in allmails:
            tmp = set()
            name = ""
            if mail in visted:
                continue
            q = deque([mail]) #acc1, acc2
            while q:
                cur_mail = q.popleft() #top is mail
                
                if cur_mail in visted:
                    continue
                visted.add(cur_mail)
                for g_id in group[cur_mail]:
                    for m in accounts[g_id][1:]:
                        name = accounts[g_id][0]
                        tmp.add(m)
                        q.append(m)
            tmp = sorted(list(tmp))
                
            res += [[name] + tmp]
            
        return res
            
                
