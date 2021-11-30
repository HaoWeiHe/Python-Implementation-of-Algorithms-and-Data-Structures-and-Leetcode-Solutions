class Solution(object):
    def canJump(self, nums):
        """
        [2,3,1,1,4]
           v
maxL     2 4
        """
        
        maxL = 0
        for i,v in enumerate(nums):

            if i > maxL:
                return False
            maxL = max(maxL,i + v)
        return True
                
            
    
