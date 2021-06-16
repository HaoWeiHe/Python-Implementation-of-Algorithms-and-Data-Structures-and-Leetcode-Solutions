class Solution(object):
    def nextPermutation(self, nums):
        """
        12587
          ^ first decline number
           -> find the small but larger 
        [1,3,2]
        """
        n = len(nums)
        first_declin_idx = n 
        for idx in range(n-2,-1,-1):
            if nums[idx] < nums[idx+1]:
                first_declin_idx = idx
                break
        if first_declin_idx == n:
            nums.reverse()
            return nums
        # [1,2,3]
        smallest_idx = n
        smallest_val = float('inf')
        for idx in range(n-1,first_declin_idx, -1):
           
            if nums[idx] > nums[first_declin_idx] and nums[idx] < smallest_val:
                smallest_idx = idx
                smallest_val = nums[idx]
      
        nums[smallest_idx], nums[first_declin_idx] = nums[first_declin_idx], nums[smallest_idx]
       
        for idx, val in enumerate(sorted(nums[first_declin_idx+1:])):
            nums[first_declin_idx+1 + idx] = val
        
        return nums
        