class Solution(object):
    def search(self, nums, target):
        """
        
        [4] 5  [6 1 2 3]
          ^
         5 is not a pivot (5 > 6)
         4 < 5, find right
        [6 1 2 3]
           ^
         1 is not 
         6 > 1 , find left
         
         
        1. check if poviot point, (cmp cur and cur + 1) #if cur == end, just return 0
        2. compre 4 (first) & 5, if  5 > target, find left (else find right)
        3. 
        1) find the smallest
        2) use binary search
        if L_val < target: (L_val ~ min_idx]
        else: (min_idx ~ R]

        """
        if not nums:
            return -1 

        def getpivot(l,r):
            if nums[l] <= nums[r]:
                return 0
            while l <= r:
                m = l + (r-l) / 2
                if nums[m] > nums[m + 1]:
                    return m + 1
                if nums[m] < nums[l]:
                    r = m -1
                else:
                    l = m + 1

        def bs(l,r):
            while l < r:
                m = l + (r - l)/2
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    r = m
                else:
                    l = m + 1
            return -1
        
        min_idx = getpivot(0, len(nums)-1)
        if min_idx ==0 :
            return bs(0,len(nums))
        
        if nums[0] <= target:
            return bs(0, min_idx)
       
        return bs(min_idx, len(nums))
