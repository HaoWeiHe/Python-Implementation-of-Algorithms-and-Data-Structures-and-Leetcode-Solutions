class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        m,n = len(mat), len(mat[0])
        def getdiag(i,j):
            target = i 
            ans = []
            while True:
               
                ans.append(mat[i][j])
                i +=1
                j -= 1
                if i >=m or j < 0: 
                    break
            return ans
        
        counter = 0 
        i = 0 
        def _iterate(i,j):
            if counter %2 == 0:
                ans.extend(getdiag(i,j)[::-1])
            else:
                ans.extend(getdiag(i,j))           
        for j in range(n):
            
            _iterate(0,j)
            counter += 1
        for i in range(1,m):
            _iterate(i,j)
            counter += 1
            
        return ans