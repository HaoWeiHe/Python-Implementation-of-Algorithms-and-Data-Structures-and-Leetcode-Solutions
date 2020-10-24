class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = collections.Counter(ages)
        # {1:3,2:4}
        res  = 0 
        for ageA, countA in count.items():
            for ageB, countB in count.items():
                if ageB > ageA or ageB <= 0.5*ageA +7 or (ageB > 100 and ageA < 100):
                    continue
                res += countA * countB
                if ageA == ageB: 
                    res -= countA
        return res

# class Solution(object):
#     def numFriendRequests(self, ages):
#         """
#         :type ages: List[int]
#         :rtype: int
#         """
#         res = 0
#         n = len(ages)
       
#         # print(ages)
#         for A in range(n):
#             for B in range(n):
#                 if A == B: continue
                
#                 if ages[B] > ages[A] or ages[B] <= 0.5*ages[A] +7 or (ages[B] > 100 and ages[A] < 100):
#                     continue
#                 res = res + 1
#         return res
