class Solution(object):
    def firstMissingPositive(self, nums):
        """
        [0,1,2]
         
        """
        if not nums: return 1
        nums = sorted(list(set(nums)))
        
        #[-1,0,1, 3]
        # 0  1 2 3
        start_idx = -1
        for idx, n in enumerate(nums):
            if n <= 0:
                start_idx = idx
            else:
               
                if n != (idx-start_idx):return idx-start_idx
        if nums[-1] < 0 :return 1
        return 1+ nums[-1]