class Solution(object):
    def maximalRectangle2(self, matrix):
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

    def maximalRectangle(self, matrix):
        """
        compute the max reactangle row by row
        [
        ["1","0","1","0","0"],
        ["2","0","2","1","2"],
        ["3","1","3","2","3"],
        ["4","0","0","3","0"]]
        
        for c in cols:
            lst = []
            for r in row:   
                maxtric_ij = maxtric_ij-1 + 1 if == "1" else 0
                lst.append(maxtric_ij)
                
            max_result compute_height_histragram(lst)
        return max_result
        """
        
        if not matrix:return 0
        rows,cols  = len(matrix), len(matrix[0])
        
                
        def compute_height_histragram(lst):
            if not lst:
                return 0
            lst = [0] + lst
            """
            lst = [1,3,5,2,7]
            lst = [0,1,3,5,2,7]
            
            [0,1,2,] i = 3
            [0,1]  loc = lst[2]*(3-top-1) = 5, max = 5
            [0]   loc = lst[1] * (3-top-1) = 6, max = 6
            """

            i = 1
            ans = 0 
            s = [0]
            while i < len(lst):
                while lst[i] < lst[s[-1]]:
                    top = s.pop()
                    ans = max(ans, lst[top] *(i - s[-1]- 1))
                s.append(i)
                i += 1
            while len(s) > 1:
                top = s.pop()
                
                ans = max(ans, lst[top]*(i - s[-1] - 1)) 
            return ans
        
        matrix[0] = map(int ,matrix[0])
       
        ans = compute_height_histragram(matrix[0])
        for r in range(1,rows):
            lst = []
            for c in range(cols):
                matrix[r][c] = matrix[r-1][c] + 1 if matrix[r][c]== "1" else 0 
                lst.append(matrix[r][c])        
            ans = max(ans,compute_height_histragram(lst) )
        return ans
        