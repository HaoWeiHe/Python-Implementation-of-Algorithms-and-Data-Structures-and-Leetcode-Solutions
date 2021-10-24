class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        # [[1,3],[2,2],[3,1]]
        boxTypes.sort(key = lambda (n,u):u, reverse = True)
        ans = 0 
        for num, unit in boxTypes:
            if num < truckSize:
                ans += num*unit
            else:
                ans += (truckSize)*unit
                break
            truckSize -= num
        return ans
        