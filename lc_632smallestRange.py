from heapq import heapify, heappop
class Solution(object):
    def smallestRange(self, nums):
        """
        [
          [4,10,15,24,26],
             i
          [0,2,12,20],
             j
          [5,18,22,30]
           k
        
        cur_min  = 4,5,19
        cur_max  = 
        
         ]
         
         
        """
        hs = []
        for ele in nums:
            hs.append(heapify(ele))
        
        ans, num = None, float("inf")
        
        flag = True
        while flag:
            _mx = float('-inf')
            _mn = float('inf')
            for tree in nums:
                _mn = min(_mn, tree[0])
                _mx = max(_mx, tree[0] )
            if (_mx - _mn) < num:
                num =  (_mx - _mn)
                ans = [_mn, _mx]
            elif (_mx - _mn) == num:
                if _mn < ans[0]:
                    ans = [_mn,_mx]

            can, canidx = float("inf"), 0
            for idx, lst in enumerate(nums): #find the smallest val
                if can > lst[0]:
                    can = lst[0]
                    canidx = idx
            heappop(nums[canidx])
            
            if not nums[canidx] :
                break
            

        return ans

