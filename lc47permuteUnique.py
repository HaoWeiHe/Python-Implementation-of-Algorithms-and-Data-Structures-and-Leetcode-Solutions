class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        c = collections.Counter(nums)
        
        self.res = []
        def dfs(lst,c):
            if len(lst) == len(nums):
                self.res.append(lst)
                return
            for ele in c:
                if c[ele] > 0:
                    c[ele] -= 1
                    dfs(lst+[ele],c)
                    c[ele] += 1
        dfs([],c)
        return self.res