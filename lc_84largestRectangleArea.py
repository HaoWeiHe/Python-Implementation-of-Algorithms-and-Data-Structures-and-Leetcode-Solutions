class Solution(object):
    def largestRectangleArea(self, heights):
        """

        insert 0 at index 0:
        
        [0,2,1,5,6,2,3] #cur is the right boundery, top it the left boundery '
                        #cur should > top, if not compute the val_at_top * length
         0 1 2 3 4 5 6
        [0,1] #loc = 2 max =2 
        [0,2] #loc = 2 max =2 
        [0,2,3,4]#loc = 2 max =2 
        [0,2,3] #i = 5, loc = 6*(5-3-1) = 6 max = 6
        [0,2] #i = 5, loc = 5*(5-2-1) = 10 max = 10 
        [0,2] #i = 5, loc = 5*(5-2-1) = 10 max = 10
        [0,2,5,6] 
        
        """
        s = [0]
        i  = 1
        ans = 0 
        heights = [0] + heights
        while i < len(heights):
            cur = heights[i]
            loc = 0 
            
            while heights[s[-1]] > cur:
                top = s.pop()
                loc = max(loc, heights[top]*(i-s[-1]-1))
                ans = max(ans, loc)
            s.append(i)
            i += 1
       
        while len(s)>1:
            top = s.pop()
            ans = max(ans, heights[top]*(i-s[-1]-1))
        return ans