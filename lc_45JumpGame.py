class Solution(object):
    def jump(self, nums):
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
        