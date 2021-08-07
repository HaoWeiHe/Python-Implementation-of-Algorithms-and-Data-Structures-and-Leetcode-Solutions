class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """

        points = list(set([tuple(e) for e in points]))
        if len(points) <=1:
            return True

        """
        1 -> [-1,1]
        3 -> [-8,8]
        (-8,3)  (8,3) (-8+8 = N)
        (-1,3) (1,3)   [-8,-1, 1,8]  nlgn + n
        (-1,1)  (1,1)  (-1+1 = N)
        
        
        """
        g = defaultdict(list)
       
        for x,y in points:
            g[y].append(x)
        
        self.m = 0
        flag  = True
        def helper(lst):
            i,j = 0, len(lst)-1
            
            while i <= j:
               
                if (lst[i]+lst[j])!=self.m:
                    return False
                i +=1
                j -=1
            return True
        for _, lst in g.items():
            lst.sort()
            if flag :
                self.m = lst[0] + lst[-1]
                flag = False
            
            if helper(lst) == False:
                return False
        return True