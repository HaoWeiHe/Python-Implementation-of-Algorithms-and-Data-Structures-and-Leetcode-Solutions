class Solution(object):
    def moveZeroes3(self, nums):
        """
           r
        [0,1,0,3,12]
         w
            r
        [1,0,0,3,12]
           w
           
        """
        w = 0 
        for r in range(len(nums)):
            if nums[r] != 0 :
                nums[r], nums[w] = nums[w], nums[r]
                w += 1
        
    def moveZeroes2(self, nums):
        """
       [1,3,0,0,12]
     w      v
     r         v 
        """
        w,r = 0, 0 
        while r < len(nums) and w < len(nums):
            while w < len(nums) and nums[w] != 0 :
                w += 1
            r = w + 1
            while r < len(nums) and nums[r] == 0:
                r += 1
            if w <len(nums) and r < len(nums):
                nums[w],nums[r] = nums[r],nums[w]
            w += 1
        
    def moveZeroes(self, A):
        """
        [0,1,0,3,12]
         i
           j -> every time A[i] ==0, find j and i ++ 
         1 0 0 3 12
           i
               j
        1 3 0 0 12
            i
        1 3 0 0 12
                j
        1 3 12 0 0
               i    
        """
        i, j = 0,0 
        
        while j < len(A) and i < len(A):
            if A[i] == 0:
                j = i + 1
                while j < len(A) and A[j] == 0:
                    j += 1
                if j < len(A):
                    A[i], A[j] = A[j], A[i]
                
            i +=1    
        return A