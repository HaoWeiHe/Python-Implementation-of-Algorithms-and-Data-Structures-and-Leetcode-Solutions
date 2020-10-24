class Solution:
    # def subarraySum(self, nums, k):
    def subarraySum(self,nums, k):
        dic = dict()
        res, _sum = 0, 0 #res for return, _sum is to add in dic
        dic[0] = 1

        for elem in nums:
            _sum += elem
            if (_sum - k) in dic:
                res += dic[_sum -k]
            if not _sum in dic:
                dic[_sum] =0
            
            dic[_sum]+= 1

      
        return res