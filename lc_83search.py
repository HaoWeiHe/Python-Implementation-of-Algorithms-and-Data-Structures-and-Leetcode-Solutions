class Solution(object):
    def search(self, nums, target):
        """
        1) find the roated point (will have 2 part of sorted array)
        2) decide which part should target in (cmp /w nums[0] with target)
        """
        if not nums:
            return -1
        if target == nums[0]:
            return 0
        def findPivot(arr):
            # [4,5,6,7,0,1,2], 
            # if mid > arr[r], right part
            # if mid < arr[r], left part 
            l, r = 0, len(arr) -1
            while l < r:
                m = (l + r) /2
                if arr[m] > arr[r]:
                    l = m + 1
                else:
                    r = m
            return l 

        def find_target(base, arr):
            l, r = 0, len(arr) 
            while l < r:
                m = l + ( r - l )/2
                if target == arr[m]:
                    return m + base
                elif target > arr[m]: #right part
                    l = m + 1
                else:
                    r = m
            return -1
        m = findPivot(nums)
        if m ==0:
            m = len(nums)
        if target > nums[0]:
            #left part
            return find_target(0, nums[:m])
        if target < nums[0]:
            #right part
            return find_target( m, nums[m:])

