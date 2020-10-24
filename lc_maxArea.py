class Solution:
    def maxArea(self, height):

        res,l,r = 0, 0, len(height)-1
       
        
        while(l < r):
            
            res = max(res, min(height[r],height[l])*(r-l))

            if height[l] > height[r]:
                r -= 1
            else:
                l +=1

        return res
