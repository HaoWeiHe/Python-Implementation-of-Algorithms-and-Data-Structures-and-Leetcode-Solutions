class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
 [1  3  -1] -3  5  3  6  7       3
 tmp = 3
 1 [3  -1  -3] 5  3  6  7       3
 [3]
 1  3 [-1  -3  5] 3  6  7       5
 reconsider 
 [5]
 1  3  -1 [-3  5  3] 6  7       5
 [5]
 1  3  -1  -3 [5  3  6] 7       6
 [5]
 1  3  -1  -3  5 [3  6  7]      7
 reconsider
        """
        q = deque(nums[:k])
        ans = [max(nums[:k])]
        tmp = ans[0]
        for e in nums[k:]:    
            
            top = q.popleft()
            q.append(e)
            
            if top != tmp:
                tmp = max(tmp, e)
            else:
                # reconsider
                tmp = max(q)
            
            ans.append(tmp)
        return ans