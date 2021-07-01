class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
                    "00110"
                       i
        make all zoeros in range 0~i , allones in range(i, n-1)
        allones:     f(i) =f(i+1) + 1 if i == "0" 
        allzeros:    f(i) = f(i-1) + 1 if i == "1"
        loop 1, n-1, find min allones(i) +allzeros(i) as tmp_ans
        return min(tmp_ans, allones[0])
        
        """
        n = len(s)
        ones, zeros = [0] * n, [0] *n
        ones[-1] = 1 if s[-1] == "0" else 0
        zeros[0] = 1 if s[0] == "1" else 0
       
        for i in range(n-2,-1,-1):
            ones[i] = ones[i+1] + 1 if s[i] == "0" else ones[i+1]
        for i in range(1,n):
            zeros[i] = zeros[i-1] + 1 if s[i] == "1" else zeros[i-1]
       
        ans = min(ones[0],zeros[-1])
        for i in range(1,n):
            ans = min(ans, zeros[i-1] + ones[i])
        
        return ans
