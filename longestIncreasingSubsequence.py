class Solution(object):
    

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
   
#  2, 5, 3, 7, 101  
        
# Res >>   2, 3, 7,101          
# MinLen>> 0, 1, 1, 2,
 

        
        # for i in len(n)
            # if n[i] >  Res[MinLen], Res[len(Res)+1] = n[i]
            # else search the locate that in the left node is small then n[x] and the right node is larget then n[x+1]
        
        if not nums:
            return 0
        
        
        Res = []
        Res.append(nums[0]) # as boundary number
        
        
        
        for i in range(1,len(nums)):
            num = nums[i]
            # print(Res)
            if num > Res[-1]:
                Res.append(num)

                
            else:
                
                for idx in range(len(Res)):
                    if Res[idx] >= num:
                        Res[idx] = num
                        break

        return len(Res)
                    
                    
                