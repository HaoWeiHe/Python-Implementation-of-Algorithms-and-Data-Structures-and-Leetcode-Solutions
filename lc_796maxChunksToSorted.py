from heapq import  heappop, heappush

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        arr[:K+1] == [0,..,K]
        
       
    max  0 1 2 3 4
    ans  0 1 2 3 4
        [4,3,2,1,0]
         0 1 2 3 4
    max = 4 4 4 4 4
    anx = 0 0 0 0 0
        
        [1,0,2,3,4]
         0 1 2 3 4
    max  1 1
    
        """  
        mx = 0 
        ans = 0
        for idx,e in enumerate(arr):
            mx = max(mx, e)
            if mx == idx:
                ans += 1
        return ans
            
       