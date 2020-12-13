import random

class Solution(object):
    def kClosest(self, lst, K):
        dist = lambda i : lst[i][0]**2 + lst[i][1]**2
        
        def sort(i,j,lst, K):
            """
            [5, 17545, 52, 61, 41, 65]
             65 17545, 52, 61, 41 | 5
             mid = 1
             5 65 17545, 52, 61, 41

            """
          
            if i < j :
                pivot = random.randint(i,j)
                
                lst[j], lst[pivot] = lst[pivot], lst[j]
                
                mid = partition(i,j,lst)
                if  K < mid - i + 1:
                    sort(i,mid - 1,lst, K)
                elif K > mid - i + 1:
                    sort(mid + 1,j,lst, K - (mid -i +1)) 

        def partition(lo,hi,lst):
            pivot = hi
            i = lo - 1
            
            for j in range(lo, hi): 
                if dist(j) < dist(pivot):
                    i += 1
                    lst[i], lst[j] = lst[j], lst[i]
            i += 1 
            
            lst[i], lst[pivot] = lst[pivot], lst[i]
            return i 
        
        sort(0, len(lst)-1,lst,K)
        return lst[:K]
  
    def kClosest2(self, lst, K):
        """
        :type lst: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        h = []
        for p in lst:   
            distance = p[0] **2 + p[1] **2
            heapq.heappush(h,(distance, p))
        
        return [heapq.heappop(h)[1] for _ in range(K)]