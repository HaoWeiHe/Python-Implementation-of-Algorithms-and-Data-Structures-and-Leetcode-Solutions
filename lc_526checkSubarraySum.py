class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        k = 13
        2 5 33 6 7
        (2,0),(7,1),(1,2)(7)
        
        (0,1) (1,1) 
        """
        h = {0:-1}
        tmp = 0 
        for i,v in enumerate(nums):
            tmp +=v
            if k :
                tmp = tmp % k
            if tmp in h: 
                if i - h[tmp] > 1:
                    return True
            else:
                h[tmp] = i
        return False