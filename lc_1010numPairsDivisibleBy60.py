
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        speed up : two sum
        1) [0,20,150,100,40] mod by 60 
        2) search for if 60-cur is exsit
        [30, 20, 30, 40, 40]
         30:2, 20:1,40:1
        
        """
        
        d = collections.defaultdict(int)
        res = 0

        for t in time:
            
            if (60 - t) % 60 in d :
                res += d[( 60 - t)%60]
            
            d[ t % 60 ] += 1
        return res
