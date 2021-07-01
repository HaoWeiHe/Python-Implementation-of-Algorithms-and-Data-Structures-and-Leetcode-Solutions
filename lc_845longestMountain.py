
class Solution(object):
    def longestMountain(self, arr):
        """
         [2,1,4,7,3,2,5,1]
    left    0 1 2 2 2 0
    right   0 0 0 1 2 0
       
       [0,1,2,3,4,5,4,3,2,1,0]
                  4
                  4
        """
        ans = left = right = 0
        
        n = len(arr)
        for i in range(1,n):
           
            if right and arr[i] > arr[i-1] or arr[i-1] == arr[i]:
                right, left = 0, 0 
                
            left += int(arr[i] > arr[i-1])
            right += int(arr[i] < arr[i-1])
            if right and left:
                ans = max(ans, left + right + 1)
        return ans
        
    def longestMountain2(self, arr):
        """
        dp[i]: 
            a[j], a[j+1],..., a[i] less than arr[i]
            a[i+1], a[i+2], ..., a[k]
        [2,1,4,7,3,2,5]
         1 1 2 3 1 1 0
         0 2 1 3 2 1 1 
         
         [2,2,2]
          0 0 0
          0 0 0
          
        [2,1,4,7,3,2,5]
         0 0 1 2 0 0 
           0 0 2 1 0 0
        arr[j] ... a[i] ... a[k]
    -> from left, dp[i] = dp[i-1] + 1 if > before, else, 1
    -> from right: 
        
        """
        n  = len(arr)
        right = [0] * n 
        left = [0] * n 
        
        
        for i in range(1,n):
            right[i] = right[i-1] + 1 if arr[i] > arr[i-1] else 0
        
        for i in range(n-2,-1,-1):
            left[i] = left[i+1] + 1 if arr[i] > arr[i+1] else 0
        
        ans= 0 
        
        for i in range(1,n-1):
            if right[i] and left[i]:
                ans = max(ans, right[i] + left[i] )
        
        return ans + 1 if ans  else 0 
        