class Solution(object):
    def findLength(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        mem = [[0] *(len(B)+1) for _ in range(len(A)+1)]
        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    mem[i][j] = mem[i+1][j+1] + 1
        return max([max(e) for e in mem])
       