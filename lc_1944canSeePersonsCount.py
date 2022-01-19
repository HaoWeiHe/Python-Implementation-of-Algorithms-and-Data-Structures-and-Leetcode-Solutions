class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        
        [10,6,8,5,11,9]
              ^
stack   [0(10)]
ans     [1,]

           
        """
        s, ans = [], [0] * len(heights)
        for i, v in enumerate(heights):
            while s and v > heights[s[-1]]:
                ans[s.pop()] += 1
            if s:
                ans[s[-1]] += 1
            s.append(i)
        return ans
        