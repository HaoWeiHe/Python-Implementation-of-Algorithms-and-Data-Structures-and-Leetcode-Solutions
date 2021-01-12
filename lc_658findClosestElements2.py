class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        1.bfs
        2. 3  <- x -> 2 
           i            j
           [1,2,8,9]
            0 1 2 3  4
              i      j 
           j-i-1  == k 
        """
        def getidx():
            l,r = 0, len(arr)
            while l < r:
                m = (l+r)//2
                if arr[m] > x:
                    r = m
                else:
                    l = m + 1
            return l 

        idx = getidx()
        
        i,j = idx -1, idx 
        while 0 <= i and j < len(arr) and j-i -1 < k:
            if abs(x - arr[i]) <= abs(arr[j] - x):
                i -= 1
            else:
                j += 1
        
        rem = k - (j-i -1)
        
        if i < 0:
            j += rem
        else:
            i -= rem
        return arr[i+1:j]
