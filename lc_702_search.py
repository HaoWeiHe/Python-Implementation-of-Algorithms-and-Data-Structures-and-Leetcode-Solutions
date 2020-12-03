
class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        
        l,r = 0, 1

        while reader(r) < target:
            l = r
            r = r << 2

        while l <= r:
            mid = (l+r)/2
            midv = reader.get(mid)
            if  midv == target:
                return mid
            if midv > target:
                r -=1
            else:
                l +=1
        return -1








