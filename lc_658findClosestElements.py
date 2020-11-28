import heapq, collections
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        use heap and dicionary : 
        [distance, obj],  {obj:[ordered lst]}
        2 1
        1 2
        0 3
        1 4
        """
        h = []
        dct = collections.defaultdict(list)
        for e in arr:
            distance = abs(e-x)
            if distance in dct:
                dct[distance].append(e)
            else:
                dct[distance].append(e)
                heapq.heappush(h,(abs(e-x),dct[distance]))
        res = []
        # print(dct)
        while h:
            distance, lst = heapq.heappop(h)
            res += lst
            
            if len(res) >= k:
                break

        return sorted(res[:k])
        
