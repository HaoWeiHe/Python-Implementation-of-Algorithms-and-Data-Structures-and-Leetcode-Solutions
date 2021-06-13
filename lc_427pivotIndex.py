class Solution(object):
    def pivotIndex(self, nums):
        """
        [1,7, 3, 6, 5, 6]
         1 8 11 17 22 28
                v
leftsum = 1 8 11
sum = 46
rithsum = 46 - cur - leftsum = 46 - 17 - 11
    
         
        """
        allS = sum(nums)
        pres = 0
        for idx, e in enumerate(nums):
            if allS - pres - e == pres:
                return idx
            pres += e
        return -1
        
        