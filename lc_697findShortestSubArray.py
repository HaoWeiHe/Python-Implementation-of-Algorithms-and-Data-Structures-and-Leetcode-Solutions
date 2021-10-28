class Solution(object):
    def findShortestSubArray(self, nums):
        """
         [1,2,2,3,1]
          0 1 2 3 4
         1:[0,4]
         2:[1,2] -> here
         3:[3]

         max = 2

         
        """
        if not nums:
            return 0
        d = defaultdict(list)
        degree = 0 
        for idx, val in enumerate(nums):
            d[val].append(idx)
            degree = max(degree, len(d[val]))

        ans = float('inf')
        for ele in d.values():
            if len(ele) == degree:
                ans = min(ans, ele[-1] - ele[0] + 1)
        return ans 
        