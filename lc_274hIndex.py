class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n = len(citations)
        citations.sort(reverse = True)
        for h in range(n,-1,-1):
           
            counter = 0 
            for e in citations:
                if e < h:
                    break
                counter +=1
           
            if counter >= h :#and (n - counter) <= h:
                return h
        return 0
            
    

