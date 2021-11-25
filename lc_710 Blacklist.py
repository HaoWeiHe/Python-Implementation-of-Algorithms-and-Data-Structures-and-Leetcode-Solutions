class Solution(object):

    def __init__(self, n, lst):
        """
        [0,1,2,3,4,5,6,7]
                 ^
                   
            x     4-x
        if block = [0,1,2,4]
        {0:5} {1:6}
        
         
        """
        lst.sort()
        self.d, self.lgth = {}, n - len(lst)
        idx = 0 
        self.s = set(lst)
        for ele in range(self.lgth, n):
            if ele not in self.s:
                self.d[lst[idx]] = ele
                idx += 1

    def pick(self):
        """
        :rtype: int
        """
        picked = random.randint(0, self.lgth-1)
        return self.d[picked] if picked in self.d else picked
        
        
    

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()