class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if  nums:
           
            self.accumulate = [nums[0] ]
            
            for idx in range(1,len(nums)):
                self.accumulate.append(self.accumulate[- 1] + nums[idx])
      
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accumulate[j]  - self.accumulate[i-1] if i-1 >= 0 else self.accumulate[j] 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)