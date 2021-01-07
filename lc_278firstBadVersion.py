# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        [l,r)
        l : the first bad version
        """
        l,r = 0, n + 1
        
        while l < r:
            m = (l+r)/2
            if isBadVersion(m):
                r = m  #[l,m)
            else:
                l = m + 1 #[m+1,r)
        return l 
        