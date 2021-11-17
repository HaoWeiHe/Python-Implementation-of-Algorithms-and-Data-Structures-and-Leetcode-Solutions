from heapq import heapify, heappop, heappush
class Solution(object):
    def smallestRange(self, nums):
        """
        [
          [4,10,15,24,26],
           i
          [0,9,12,20],
             j
          [5,18,22,30]
           k
         ]
         
        (0,5) -> num, ans = 5, ans(0,5)
        (4,9) -> num, ans = 5, ans(4,9) > need cmp 4 and 0 if equal
         
        """
        h = []
        tmax, tmin = max([l[0] for l in nums]), min([l[0] for l in nums])
        ans = [tmin, tmax]
        for gid, lst in enumerate(nums):
            heappush(h, (lst[0], gid,0))

        while h:
            val, gid, idx = heappop(h)
            

            if len(nums[gid]) -1 > idx:
                heappush(h,(nums[gid][idx + 1], gid, idx +1))
                tmax = max(tmax, nums[gid][idx + 1])
            
            if not h:return ans
            tmin =  h[0][0]

            if len(nums[gid]) -1  == idx and h[0]!=val:
                return ans 
            if tmax - tmin < ans[1] - ans[0]:
                ans = [tmin, tmax]
            elif tmax - tmin == ans[1] - ans[0] and tmin < ans[0]:
                ans = [tmin, tmax]
     
        return ans



        


nums = [[[1]],[[-89,1,69,89,90,98],[-43,-36,-24,-14,49,61,66,69],[73,94,94,96],[11,13,76,79,90],[-40,-20,1,9,12,12,14],[-91,-31,0,21,25,26,28,29,29,30],[23,88,89],[31,42,42,57],[-2,6,11,12,12,13,15],[-3,25,34,36,39],[-7,3,29,29,31,32,33],[4,11,14,15,15,18,19],[-34,9,12,19,19,19,19,20],[-26,4,47,53,64,64,64,64,64,65],[-51,-25,36,38,50,54],[17,25,38,38,38,38,40],[-30,12,15,19,19,20,22],[-14,-13,-10,68,69,69,72,74,75],[-39,42,70,70,70,71,72,72,73],[-67,-34,6,26,28,28,28,28,29,30,31]],[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], [[1,2,3],[1,2,3],[1,2,3]],[[10,10],[11,11]],[[10],[11]],[[1],[2],[3],[4],[5],[6],[7]]]
ans = [[1,1],[13,73],[20,24],[1,1],[10,11],[10,11],[1,7]]
for idx, val  in enumerate(nums):
 
    print("{}\t{}".format(ans[idx], Solution().smallestRange(val)))