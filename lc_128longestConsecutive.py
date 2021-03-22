class Solution(object):
    def longestConsecutive(self, nums):
        """
        [100,4,200,1,3,2]
        
        """
        
        h = set(nums)
        tmp, ans = 0,0
        for e in h:
            if e -1 not in h:
                tmp = 0

                c = 0

                while e + c in h:
                    tmp += 1
                    c += 1

                ans = max(ans, tmp)
        return ans
                
        
    def longestConsecutive3(self, nums):
        """
       [100,4,200,1,3,2]
       [1,2,3,4,100,200]
    tmp 1 
    ans 1 2  3 4 1  2
        
        [0,3,7,2,5,8,4,6,0,1]
        
    
        """
        if not nums:return 0
       
        nums.sort() #nlogn
        tmp, ans = 1,1
        for idx, e in enumerate(nums):
            if idx ==0:
                continue
            if e == nums[idx-1]:
                continue
            elif e == nums[idx-1] + 1:
                tmp +=1
            else:
                tmp = 1
      
            ans = max(ans, tmp)
        return ans
        
    def longestConsecutive2(self, nums):
        """
       [100,4,200,1,3,2]
       [1,2,3,4,100,200]
    tmp 1 
    ans 1 2  3 4 1  2
        
        [0,3,7,2,5,8,4,6,0,1]
        
    
        """
        nums = list(set(nums))
        nums.sort() #nlogn
        tmp, ans = 1,0
        for idx, e in enumerate(nums):
            if idx == 0 or e != (nums[idx-1] + 1) :
                tmp = 1
            else:
                tmp +=1
            ans = max(ans, tmp)
        return ans
        