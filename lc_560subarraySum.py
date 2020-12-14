class Solution(object):
    def subarraySum(self, nums, k):
        """
         [3,4,7,2,-3,1,4,2] , k = 7
    h =  {0:1, 3:1, 7:1, 14:2, 16:1, 13:1}
    acc = 3 7 14 16 13 14
acc-k=   -4,0 7   9  6 7
    ans = 0 1 2   2  2 3
"""
        h = collections.defaultdict(int)
        acc = 0 
        ans = 0
        h[0] = 1
        
        for e  in nums:
            acc += e
            ans += h[acc -k ]
            h[acc] +=1
        return ans
        