class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        N = (x+1) + (x+2) + (x+3) + .. + (x+k)
        N = kx+ (1+k)*k/2
        x =  (N -(1+k)*k/2)/k
        if N = 15
        if k ==1, x = 14
        if k = 2, x = 5
        if k = 3, x = 3 
        if k = 4, x not a int
        if k = 5, x= 0
        
        -> x should be an integer, and larger than 0 and less than N-1
        """
        if N ==1:
            return 1
        count = 0
        for k in xrange(1, N):
            x = (N - (1+k)*k/2.0)/k
            if 0 <= x < N and x == int(x):
                count +=1
            if x < 0:
                break
        return count
            