import collections
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
   
       -> direted graph /w set_pair
       -> ind = {1:1,2:1,3:1,4:0,5:1,6:1}
       c = 0
       while q :
            if len(q) >1: False
            top = q.popleft()
            c +=1
            for e in g:
                e.ind -=1
                if e.ind is 0: append to q
        return 1 if c == len(org) else 0 
        """
        
        allins = set([e for s in seqs for e in s ])
        if len(allins) != len(set(org)):return False
        ind = collections.defaultdict(int)
        g = collections.defaultdict(set)
        for seq in seqs:
            for a,b in zip(seq, seq[1:]):
                if b not in g[a]:
                    ind[b] += 1
                g[a].add(b)
                

        q = collections.deque([e for e in allins if e not in ind])
        
        res = []
        while(q):
            if len(q) > 1: 
                return False
            cur = q.popleft()
            res.append(cur)
            for ele in g[cur]:
                ind[ele] -= 1
                if ind[ele] ==0:
                    q.append(ele)
      
        return True if res == org else False
