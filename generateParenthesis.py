class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        if not n :
            return n
        
        def helper(right, left, tmp,n):

            if right == n :
                res.append(tmp)

            if left < n :
                helper(right, left+1, tmp + "(",n)

            if right < left :
                helper(right +1, left, tmp+")",n)

        
        helper(0,0,"",n)
        return res

    
    