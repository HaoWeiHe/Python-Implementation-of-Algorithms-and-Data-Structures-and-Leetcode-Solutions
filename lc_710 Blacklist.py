from random import randrange
class Solution(object):

    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        self.n = n
        self.s = [v for v in range(n) if v not in set(blacklist)]

    def pick(self):
        """
        :rtype: int
        """
        return random.choice(self.s)
     


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()