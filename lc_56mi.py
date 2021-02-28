class Solution(object):
    def merge(self, its):
        """
        [[1,3],[2,6],[8,10],[15,18]]
        3 between (2,6]
        1, 6
        8,10
        15,18
        
        1 4 4 5
        4 between (4,5]
           [[1,3],[2,6],[8,10],[15,18]]
    res =  [1,3]  [1,6] [8,10]  
    top =  [1,3]  [1,6] 
                        if not in append(top and itself)
        """
        its.sort(key = lambda x : (x[0],x[1]))
        if not its:return 0
        res = [its[0]]
        for ele in its[1:]:
            top = res.pop()
            if ele[0] <= top[1] <= ele[1] or top[0] <= ele[1] <= top[1]:
                top = [min(top[0], ele[0]), max(top[1],ele[1])]
                res.append(top)
            else:
                res.append(top)
                res.append(ele)
        return res
            