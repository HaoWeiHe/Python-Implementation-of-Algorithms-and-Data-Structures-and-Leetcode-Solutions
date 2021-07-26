from heapq import heappop, heappush
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        
        d = defaultdict(list)
        for student, score in items:
            heappush(d[student], score)
            if len(d[student]) > 5:
                heappop(d[student])
    
        return [[idx, sum(v)/len(v)] for idx,v in d.items()]