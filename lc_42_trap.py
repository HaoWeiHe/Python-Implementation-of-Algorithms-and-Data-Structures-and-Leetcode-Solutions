class Solution(object):
    def trap(self, height):
        """
        sum of (difference between left_max, and right_max - cur_ele) is the answer.
        """
        left_max, right_max, diff = [],[0 for _ in height], []
        cur_max = 0
        
        for ele in height:
            cur_max = max(cur_max, ele)
            left_max.append(cur_max)
        
        cur_max = 0
        for idx,ele in enumerate(height[::-1]):
            cur_max = max(cur_max, ele)
            right_max[~idx] = cur_max        
        
        for idx, ele in enumerate(height):
            diff.append(min(left_max[idx], right_max[idx]) - ele)
        
        return sum(diff)