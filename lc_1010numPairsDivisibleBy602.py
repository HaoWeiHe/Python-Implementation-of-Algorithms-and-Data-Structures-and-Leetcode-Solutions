class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        ans=0
        d=defaultdict(int)
        for e in time:
            if e%60==0:
                ans +=d[0]
            else:
                ans +=d[60-(e%60)]
            d[e%60]+=1
        return ans
        