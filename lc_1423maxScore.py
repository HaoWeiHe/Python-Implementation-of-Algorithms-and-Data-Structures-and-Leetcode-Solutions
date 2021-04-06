
class Solution(object):
    def maxScore(self, lst, k):
        """
        [1,79,80,1,1,1,200,1]
        v v v v (4,0)
        [1,79,80,1,1,1,200,1]
         v v   v           v (3,1)           
         [1,79,80,1,1,1,200,1]
          v v            v  v (2,2)

        """
        best = score = sum(lst[:k])
        for i in range(1,k + 1):
            score =  score - lst[k-i] + lst[-i]
            best = max(best, score)
        return best
    def maxScore2(self, lst, k):
        """
        [1,2,3,4,5,6,1],
         i     j
         
 tmp 6
 mn = 6
 
        [1,79,80,1,1,1,200,1]
         i         j
            i         j
                i         j
                  i         j
         
         remove the window size of n-k subarry 
         return sum - sum((n:k+1))
         
         -> max n_k subarry
        """
        if not lst:
            return 0
        if k >= len(lst):
            return sum(lst)
        
        presum = [lst[0]]
        for i in range(1, len(lst)):
            presum.append(presum[i-1] +lst[i])
        
        i,j = 0, len(lst) - k -1
        
        mn = float("inf")
        while j < len(lst):
            if i ==0:
                mn = min(mn,presum[j])
            else:
                mn = min(mn, presum[j] - presum[i-1])
            i +=1 
            j +=1 
            
        return sum(lst) - mn