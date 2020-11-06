class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix: return 0
        n = len(matrix)
        h = []
        for i in range(n):
            for j in range(n):
                heapq.heappush(h,-matrix[i][j])
                if len(h) > k:
                    heapq.heappop(h)
        return -1 * heapq.heappop(h)
                
                
        