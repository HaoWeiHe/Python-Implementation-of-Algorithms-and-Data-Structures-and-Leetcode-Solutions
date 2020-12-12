class Solution(object):
    def trap(self,height):
        lf, rt = 0, len(height) - 1
        lf_max, rt_max = 0,0
        ans = 0 

        while lf < rt:
            if height[lf] < height[rt]:
                lf_max = max(lf_max, height[lf])
                ans += (lf_max - height[lf] )
                lf +=1
            else:
                rt_max = max(rt_max, height[rt])
                ans += (rt_max - height[rt])
                rt -=1
        return ans
    # def trap2(self, height):
    #     """
    #     sum of (difference between left_max, and right_max - cur_ele) is the answer.
    #     """
    #     left_max, right_max, diff = [],[0 for _ in height], []
    #     cur_max = 0
        
    #     for ele in height:
    #         cur_max = max(cur_max, ele)
    #         left_max.append(cur_max)
        
    #     cur_max = 0
    #     for idx,ele in enumerate(height[::-1]):
    #         cur_max = max(cur_max, ele)
    #         right_max[~idx] = cur_max        
        
    #     for idx, ele in enumerate(height):
    #         diff.append(min(left_max[idx], right_max[idx]) - ele)
        
    #     return sum(diff)