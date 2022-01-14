class Solution(object):
    def findKthPositive(self, arr, k):
        """
        1 2 3 4 5 #without missing
        2 3 4 7 11
              3 
              7 + (k-3) = 9 find the point, whos difference <= k 

        """
        def getLeft():
            l, r = 0, len(arr)
            while l < r:
                mid = (l + r) / 2
                if (arr[mid] - (mid + 1)) >= k:
                    r = mid 
                else:
                    l = mid + 1
            return l-1
        anchor = getLeft()
        
        return arr[anchor] + k - (arr[anchor] - anchor - 1)
                    
        