from bisect import bisect
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        [0,1,3,50,75]
        lower = 0
        upper= 99
        
        append lower if not num or num[0]!=0
        append upper if num[-1] != upper
        [0,1,3,50,75]
        cur for 1 , cut ++
        2 ->indx(2) which have the right nib and nib = 2 +1
        4 -> indx(3) -> which the right nib not 4+1 :
        4 -> its right nibor
        cur = its right nibor + 1
        51 -> indx(5)  whcih the  which the right nib not 51+1 :
        51 -> 75
        """
     
        if not nums or nums[-1]!=upper:
            nums.append(upper+1)
        cur = lower
        res = []
       
        while cur <= upper:
            if cur in nums:
                cur +=1
            else:
                insert_idx = bisect(nums,cur)
                
                if nums[insert_idx ] == cur+1:
                    res.append(str(cur))
                    cur  +=1 
                else:
       
                    res.append("{}->{}".format(cur, nums[insert_idx ]-1 ))
                    cur = nums[insert_idx ] +1
        return res
