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
            #[4 5] [6 1 2 3]
            # if lst[l] < lst[r], sorted! return lst[l]
            # if r-l >= 1 return  min(lst[l], lst[r])
            #mid = l + (r - l)/2
            # return getpivot(l, mid) getpivot(mid+1, r)
            if r -l <= 1:
                if nums[l] < nums[r]:
                    return nums[l], l 
                else:
                    return nums[r], r
                
            if nums[l] < nums[r]:
                return nums[l], l
            m = l + (r-l)/2
            lf, lf_idx = getpivot(l,m)
            rt, rt_idx = getpivot(m+1, r)
            if rt > lf:
                return lf, lf_idx
            return rt, rt_idx

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
        
        min_idx = getpivot(0, len(nums)-1)[1]
        print(min_idx,"ew")
        if min_idx ==0 :
            return bs(0,len(nums))
        
        if nums[0] <= target:
            return bs(0, min_idx)
       
        return bs(min_idx, len(nums))
nums, target = [1],0
print(Solution().search(nums, target))