

class Solution(object):
    def nthUglyNumber(self, n, a, b, c):

        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a % b)
        def possible(mid):
            return (mid / a + mid/b + mid/c - mid/ac - mid/bc - mid/ab + mid/abc) >= n
        ab = a * b / gcd(a,b)
        bc =  b*c / gcd(b,c)
        ac = a*c / gcd(a,c)
        abc = a * bc / gcd(a,bc)
        
        l, r = 1, 10**10
        while l < r:
            mid = l + (r - l ) / 2
            if possible(mid):
                r = mid
            else:
                l = mid  + 1
        return l
        