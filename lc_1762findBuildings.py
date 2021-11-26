class Solution(object):
    def findBuildings(self, heights):
        """
        [4,2,3,1]
         ^
    max      3  1
    ans = [3,2,0] return revise version
        """
        tmp_max = 0 
        ans = []
        for i in range(len(heights)-1,-1,-1):
            val = heights[i]
            if val > tmp_max:
                ans.append(i)
                tmp_max = val
        return ans[::-1]