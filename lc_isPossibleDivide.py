
import collections
class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)%k!=0:return False
        
        Cnt = collections.Counter(nums) #{1:1, 2:1, 3:2..}
        # print(c[1])
        A = Cnt.keys()
        A.sort() 
        for num in A: 
            while Cnt[num] >0:
                for i in range(k):
                    
                    if (num + i) not in Cnt: return False
                    Cnt[num+i] -=1
                    if Cnt[num+i] < 0 : return False
        return sum(Cnt.values()) ==0

# [(1, 1), (2, 1), (3, 2), (4, 2), (5, 1), (6, 1)]
#(1,2,3,4,5,6)
#d{1} = 
        # for x,v in c:
        # print(c)

# nums, k = [1,2,3,3,4,4,5,6],4
nums =   [1,2,3,4]
k = 3
print(Solution().isPossibleDivide(nums, k ))