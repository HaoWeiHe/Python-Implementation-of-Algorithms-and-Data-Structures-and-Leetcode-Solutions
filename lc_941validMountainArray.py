class Solution(object):
    def validMountainArray(self, arr):
        """
          [3,5,5]
          [3,2,1]
          [1,2,3] 
               find idx every idx before it should < ele_idx
          [0,3,2,1]
           v
          
        """
        
        idx = 0 
        for i, v in enumerate(arr):
            if i == 0:
                continue
            if v < arr[i-1]:
                idx = i-1
                break
        if idx == 0 or idx == len(arr):
            return False

        for i in range(1,idx+1):
            if  arr[i-1] >= arr[i]:
                return False
       
        for i in range(len(arr)-1, idx , -1):
    
            if arr[i] >= arr[i-1]:
                return False
        return True