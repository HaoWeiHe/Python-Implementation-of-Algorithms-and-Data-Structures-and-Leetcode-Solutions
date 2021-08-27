class Solution(object):
    def countAndSay(self, n):
        """
        0: 1
        1: 1 
           v
        2: 1 1
        pre = 1
             v
        3: 2 2 1
             v 
           pre = 2
           ctr = 1
           if cur == pre:
               ctr +=1 
            else: 
            pop ctr
        4: 1211
        """
        def helper(lst):
            res = []
            
            pre, ctr = lst[0], 1
            for idx in range(1,len(lst)): #1, 1
                ele = lst[idx]
                if ele == pre:
                    ctr += 1
                else:
                    res += [str(ctr), str(pre)]
                    ctr = 1
                pre = ele
            
            res += [str(ctr),str(lst[-1])]
            return "".join(res)
                
        pre = "1"
        for i in range(2,n+1):
            pre = helper(pre) #"1"
           
        return pre