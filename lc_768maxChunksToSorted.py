class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        21 344
        12 344
        
        -> compare counter
        """
        c1, c2 = Counter(), Counter()
        ans = 0 
        for a, b in zip(arr, sorted(arr)):
            c1[a] += 1
            c2[b] += 1
            ans += c1 == c2
        return ans