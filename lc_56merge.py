class Solution(object):
    def merge(self, its):
        """
         [[1,9],[2,6],[8,10],[15,18]]
         1) sort ele[0]
         2) for i in range(n):
            if n >= after[0] merge
        [1,(6,9)]
        1,9
        1,10
        """
        
        its.sort(key= lambda x:(x[0],x[1]))
        n = len(its)
        stack = [its[0]]
        for i in range(1,n):
            cur = its[i]
            if stack[-1][1] >= cur[0]:
                stack[-1][1] = max(cur[1],stack[-1][1] )
            else:
                stack.append(cur)
     

        return stack
            