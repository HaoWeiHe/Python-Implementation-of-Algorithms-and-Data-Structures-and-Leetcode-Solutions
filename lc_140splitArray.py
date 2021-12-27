class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l, r = max(nums), sum(nums) + 1
        while l < r:
            mid =  (l + r) /2 #l + (r - l ) / 2
            accumulation, need = 0, 1

            """
             [7,2,5,10,8],
                  ^
              7 9 14 ->5
              mid = 14 -> 5
            """
            for e in nums:
                if accumulation > mid:
                    accumulation = 0 
                    need += 1
                accumulation += e
            if need > m:
                l = mid + 1
            else:
                r = mid
        return l