class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = len(nums) - 1
        step = 0 
        while cur != 0 :
            tmp = cur
            
            for i in range(cur-1, -1,-1):
                if nums[i] + i >= cur:
                    tmp = i
            if tmp == cur:
                return -1
            step += 1
            cur = tmp
        return step if cur == 0 else -1
    def jump2(self, nums):
        """
        [2,3,1,1,4]
         ^   
           | |
    (2,0)
          (3,1)
        """
        v = set()
        q = deque([[0, 0]])
        while q:
            top, steps = q.popleft()
            if top in v:
                continue
            v.add(top)
            if top == len(nums)-1:
                return steps
            for stp in range(1, nums[top] + 1):
                q.append([stp + top, steps + 1])
        return -1
        
