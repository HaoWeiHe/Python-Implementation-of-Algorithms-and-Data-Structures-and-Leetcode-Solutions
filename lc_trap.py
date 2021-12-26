class Solution(object):
    def trap(self, height):
        """
        [0,1,0,2,1,0,1,3,2,1,2,1]
        [0,1,1,2,2,2,2,3,3,3,3,3] (max from left) A
        [3,3,3,3,3,3,3,3,2,2,2,1] (max from right) B
        [1,1,1,1,1,1,1,1,1,1,1,1]
                             ~1~0
        [0,1,1,2,2,2,2,3,2,2,2,1] (min from A and B)
        [0,1,0,2,1,0,1,3,2,1,2,1] (orignial )
        [0,0,1,0,1,2,1,0,0,1,0,0]
        """
        n = len(height)
        if not height:
            return 0
        left, right = [height[0]], [height[-1]] * n 
        
        for idx in range(1,n):
            left.append(max(height[idx], left[idx - 1]))
            right[~idx] = max(height[~idx], right[~(idx - 1)])
        ans, diff = 0, []
        
        for idx in range(n):
            ans += min(right[idx], left[idx]) - height[idx]
        return ans