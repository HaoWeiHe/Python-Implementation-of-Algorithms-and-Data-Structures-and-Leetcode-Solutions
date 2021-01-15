class Solution:
    def insert(self, intervals, newInterval) :
        #update lst
        #find the idx of this lst
#         [[2,4],[5,7],[8,10],[11,13]]
        # [3,6]
        # [[2,7],[8,10],[11,13]]
        idx = 0 
        start, end = newInterval
        # insert_ele = newInterval
        res = []
        for ele in intervals:
            # print(ele[0], end)
            if ele[1] < start: #4 < 3
                idx += 1
                res.append(ele)
            elif ele[0] > end: #2 > 6
                print(ele[0])
                res.append(ele)
            else:
                start = min(start, ele[0])
                end = max(end, ele[1])
        print(start, end)
        return res[:idx] + [[start, end ]] + res[idx:]
a,b = [[2,4],[5,7],[8,10],[11,13]] , [3,6]
print(Solution().insert(a,b))
