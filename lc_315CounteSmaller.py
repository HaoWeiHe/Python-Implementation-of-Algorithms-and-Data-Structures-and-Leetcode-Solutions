class Solution(object):
    def countSmaller(self, nums):
        """
        [5,2,6,1]  
         v
         [1,2,6,5]
res = 0,1,1,2
return res[::-1]

insert to 0, res = 0
insert to 1, res = 1  res[:i] + cur + res[i:]
insert to 1, res = 1
insert to 2, res = 2  

        """
        lst = [float('inf')]
        res = [0] * len(nums)
        def insertPoint(target,lst):
            
            if not lst:return 0
            l,r = 0, len(lst) 
            while l < r:
                m = (l+r)/2
                if target < lst[m]:
                    r = m 
                else:
                    l = m + 1 
            return l 
        for i in range(len(nums)-1, -1,-1):
            insert_idx = insertPoint(nums[i],lst)
            res[i] = insert_idx
            lst = lst[:insert_idx] + [nums[i]] + lst[insert_idx:]
        return res



nums =  [5,2,6,1]
print(Solution().countSmaller(nums))