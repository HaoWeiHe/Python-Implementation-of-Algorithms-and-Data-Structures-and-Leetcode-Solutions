class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        (based 1)
        the first i jobs in k days
        | ..........   j| j+1 ... i|
            k-1 days       1 day
        T[i][k] = min(T[j][k] + max(jobDifficulty[j+1 ~ i ], T[i][k-1])
        T[0][0] = 0
        limitation: i > j >= k-1 
        """
        n = len(jobDifficulty)
        if d > n : 
            return -1
        T = [[float('inf')]* (d+1)  for _ in range(n+1)]
        T[0][0] = 0
        for i in range(1,n + 1):
            for k in range( 1,d + 1):
                md = 0
                for j in range(i-1,k-2,-1):
                    md = max(md,jobDifficulty[j])
                    T[i][k] = min(T[i][k], T[j][k-1] + max(jobDifficulty[j:i]))
        return T[n][d]
jobDifficulty = [6,5,4,3,2,1]
d = 2
print(Solution().minDifficulty(jobDifficulty,d))