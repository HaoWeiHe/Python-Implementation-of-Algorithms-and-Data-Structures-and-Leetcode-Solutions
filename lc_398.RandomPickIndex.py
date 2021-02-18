# class Solution(object):

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.d = collections.defaultdict(list)
#         for idx,e in enumerate(nums):
#             self.d[e].append(idx)

#     def pick(self, target):
#         """
#         :type target: int
#         :rtype: int
#         """
#         return random.choice(self.d[target])
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
    def pick(self, target):
        """
        [1,2,3,3,3]
             V V  V
             1/1 
               1/2 
                  1/3

        """ 
        count = 0 
        res = None
        for i, v in enumerate(self.nums):
            if v == target:
                picked = random.randint(0, count)
                # if not res:#no need for (0,0) will be initized by randint(0,0)
                #     res = i 
                if picked == 0 :
                    res = i
                count +=1
        return res

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)