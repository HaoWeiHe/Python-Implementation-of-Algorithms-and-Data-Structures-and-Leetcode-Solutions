
class Solution(object):
    def maxProduct(self, S1):
        """
        :type nums: List[int]
        :rtype: int
        """
        S2 = S1[::-1]
        for i in range(1, len(S1)):
            if not S1[i-1]  == 0:
                S1[i] *= S1[i-1] or 1 
            if not S2[i-1] == 0 :
                S2[i] *= S2[i-1] or 1
  
  
        return max(max(S1), max(S2))
        