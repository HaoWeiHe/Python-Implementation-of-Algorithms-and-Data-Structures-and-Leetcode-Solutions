class Solution(object):
    def minDistance(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        T = [[0] * (1+len(w1)) for _ in range(len(w2)+1)]
        for i in range(1,1+len(w1)):
            T[0][i] = T[0][i-1] + 1
        for i in range(1, 1+len(w2)):
            T[i][0] = T[i-1][0] + 1
       
    
        for i in range(1,len(w2)+1):
            for j in range(1,len(w1)+1):
                
                op = min(T[i-1][j], T[i][j-1], T[i-1][j-1])
                if w2[i-1]!= w1[j-1]:
                    T[i][j] = min(T[i-1][j], T[i][j-1], T[i-1][j-1])+1
                else:
                    T[i][j] = min(T[i-1][j]+1, T[i][j-1]+1, T[i-1][j-1])
        return T[-1][-1]