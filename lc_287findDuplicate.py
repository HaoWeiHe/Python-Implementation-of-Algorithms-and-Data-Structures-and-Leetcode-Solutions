class Solution(object):
    def findDuplicate(self, nums):
        """
        
        idxs  0,1,2,3,4
        nums  1,3,4,2,2
        
        1 3 2 4 2 4 2 4 2
        """
        slow = fast = nums[0]
      
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast =nums[fast]
        return fast
        
    def findDuplicate2(self, nums):
        """
        
        idxs  0,1,2,3,4
        nums  1,3,4,2,2
        
        1 3 2 4 2 4 2 4 2
        """
        slow = fast = nums[0]
      
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast =nums[fast]
        return fast
        

