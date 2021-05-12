class Solution(object):
    def maximalRectangle(self, matrix):
        """

    
    base: n~ 1
   [["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]]
  
  i = n
     0     1   2   3  4     (4-0)
    [["1","0","1","0","0"],
    ["1","0","1","2","3"],
    ["1","2","3","4","5"],
    ["1","0","0","1","0"]]
    
    [0,3,5,12] -> length
    0,0,0,0
    0,3, 6,9
    0,0,5, 10
    0,0, 5,12
    O(n^2) > O(n^3)

        """
        if not matrix:return 0
        matrix = [map(int,matrix[i]) for i in range(len(matrix))]
       
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1,n):
                if matrix[i][j]!=0 :
                    matrix[i][j] = int(matrix[i][j-1]) +1 
        
        def getArea(lst):
            n = len(lst)
            ans = 0
            for i in range(n):
                tmp = 0
                for j in range(n):
                    if lst[j] >= lst[i]:
                        tmp += lst[i]
                        ans= max(ans,tmp)
                    else:
                        tmp = 0 
            return ans
        ans = 0
        for j in range(n-1,-1,-1):
            lst = []
            for i in range(m):
                lst.append(matrix[i][j])
            ans = max(ans,getArea(lst))
        return ans
            
            
        
        