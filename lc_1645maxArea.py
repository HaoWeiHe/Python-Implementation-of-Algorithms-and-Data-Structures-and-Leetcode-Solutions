class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        find the max space of horizontalCuts #need 2 sort
        [1,2,4], h = 5 -> extend the cuts to [0,1,2,4,5]
        space: [1,1,2,1] max 2 
        find the max space of verticalCuts 
         [1,3], w = 4, extend: [0 1 3 4]
         space: [1,2,1] max = 2
         return 2*2
        """
        horizontalCuts.sort()
        verticalCuts.sort()
        preV = 0
        maxV = 0
        for e in verticalCuts:
            maxV = max(maxV, e-preV)
            preV = e
        maxV = max(maxV, w-preV)
        
        preH = 0
        maxH = 0
        for e in horizontalCuts:
            maxH = max(maxH,  e-preH)
            preH = e
        maxH = max(maxH,  h-preH)
   
        return (maxH*maxV)% (10**9 + 7)
        