class Solution(object):
    def multiply(self, A, B):
        """
        res[x][y] = A[x][:] * B[:][y]
        
        (0,0,1), (1,0,-1), (1,2,3)
        -> A_d = {0:{0},1:{0,2}} #{col, row}
        (0,0,7)
        (2,2,1)
        ->B_d = {0:{0}, 2:{2}} #{row: col}
        
        
        """
        A_d = collections.defaultdict(set)
        B_d = collections.defaultdict(set)
        m,n = len(A),len(A[0]) #2*3
        m1,n1 = len(B), len(B[0])
        res = [[0]*n1 for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    A_d[i].add(j)
        for i in range(m1):
            
            for j in range(n1):
                if B[i][j]:
                    B_d[j].add(i)
        
        for i in range(len(res)):
            for j in range(len(res[0])):
                for k in A_d[i]:
                    if k in B_d[j]:
                        res[i][j] += A[i][k] * B[k][j]
                
        return res
    def multiply2(self, A, B):
        """
       [0][0] = A00*B00 + A10*B01+A20*B02
        [0][1] = 
        
        
        [x][y] = [x][:] * [:][y]
        """
 
        m,n = len(A), len(A[0]) #2*3
        m2,n2 = len(B), len(B[0])
        res = [[0]*n2 for _ in range(m)]
        for i in range(len(res)):
            for j in range(len(res[0])):
                for k in range(n):
                    res[i][j]+= A[i][k] * B[k][j]
        return res
                
