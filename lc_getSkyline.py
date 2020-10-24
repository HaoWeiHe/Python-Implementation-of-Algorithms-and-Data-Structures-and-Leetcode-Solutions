
import collections
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings: return []
        d = collections.defaultdict(list)
        for l,r,h in buildings:
            for i in range(l,r+1):
                d[i].append(h)
        
        #if len(d[cur]) ==1, res.append((cur_idx, d[cur][0]))
        #if  first empty , append(cur_idx-1, 0)
        #if max_change, append(i-1,now_max)
        start, end = min(d.keys()), max(d.keys())
        res, mx, premx  =[], 0, 0
        # print(start, end)
        for idx in range(start, end + 1):
  
            if len(d[idx])>0: 
                mx = max(d[idx])
            else: 
                mx = 0

            if premx != mx:
                if premx < mx:
                    res.append([idx, mx])
                else:
                    res.append([idx-1, mx])

            premx = mx
        res.append([end,0])
        return res

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print("Except:{}".format([[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]))
print("Myanww:{}".format(Solution().getSkyline(buildings)))
        