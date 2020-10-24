
class Solution(object): 
    def countPrimes(self, n):
        
        if n <2:
            return 0
        
        max_number = int(n**0.5)+1
        isPrime = [True for i in range(n)]
        
        isPrime[0] = isPrime[1] = False
        res = 0
        
        for i in xrange(2,n):
            if isPrime[i]:
                p = i
                # print(p)
                for pn in xrange(p*p , n, p):
                    isPrime[pn ] = False
                    
        
        for i in xrange(n):
            res+= 1 if isPrime[i] else 0
            
        return res
    
