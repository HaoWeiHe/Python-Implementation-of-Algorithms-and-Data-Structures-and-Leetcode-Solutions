class Solution(object):
    def removeElement(self, nums, val):
        """
        [0,1,2,2,3,0,4,2], 2
                 v
        [0,1, 3]
             w
             
        [3,2,2,3], val = 3
               v
         [2,2]
            w
        """
        w = -1
        for v in nums:
            if v == val:
                continue
            w = w + 1
            nums[w]= v
           
        return w+1
        