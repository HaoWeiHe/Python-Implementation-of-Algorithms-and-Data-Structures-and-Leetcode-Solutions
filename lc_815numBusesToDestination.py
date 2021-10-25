class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        [1:0,2:0,7:0]
        7 < 2 < 1
        ^
        6- 0
        ^
        3 - 0 
         
        """
        
        if source == target:
            return 0
        g = collections.defaultdict(list)
        
#         1 : [(2,0), (7,0)]
#         7:[(1,0),(2,0),(3,1),(6,1)]
            
#         15 : [(4,1),(5,1),(19,4)]
# ele : (4,1,history)

        
        for gn, lst in enumerate(routes):
            for ele in lst:
                for others in lst:
                    if ele == others:
                        continue
                    g[ele].append((others, gn))

                    
        q = deque([(ele[0], ele[1], [ele[1]]) for ele in g[source]])
        v = set()
        
        while q:
            num, group, history = q.popleft()
            if num == target:
                    history += [group]         
                    return len(set(history))
                
            for ele, ele_g in g[num]:
                if (ele, ele_g) in v:
                    continue
                v.add((ele, ele_g) )
                q.append((ele, ele_g, history+[ele_g]))
        return -1