class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.d = collections.defaultdict(list)
        for idx,e in enumerate(nums):
            self.d[e].append(idx)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.d[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)