class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        v, i = float('-inf'),0
        for idx, val in enumerate(arr):
            if v < val:
                v = val
                i = idx
        return i