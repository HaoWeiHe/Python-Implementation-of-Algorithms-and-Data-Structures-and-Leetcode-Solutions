class Solution:
    def read(self, buf, n):
        
        """
        buf[idx] = ",,,,,,,,,,,,,,,,,,,,"
        if aaaa:
            lgth = read4(tmp)
            tmp = ["a","a","a","a"]
            lgth = 4
        we need to write all tmp's contain into buf
        (so, we need to write every char step by step. Note: at most n chars)
        """
        idx = 0
        while n:
            tmp = [""]*4
            lgth = read4(tmp)
            if lgth ==0: break

            for i in range(min(n,lgth)): #at most n chars
                buf[idx] = tmp[i]
                idx +=1
            n -= lgth
        return idx
