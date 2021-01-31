class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m,n = len(board), len(board[0])
        def find(word,i,v,x,y): #test by 0

            if word[i]!=board[x][y]:
                return False

            if i == len(word)-1: 
                return True

            res = False
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = dx + x, dy + y 
                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in v:
                     res = res or find(word, i+1,v + [(x,y)], nx,ny)
            return res
            
        ans = []                
        for w in words:
            flag = True
            for i in range(m):
                for j in range(n):
                    if board[i][j] == w[0] and flag:
                        if find(w,0,[],i,j):
                            
                            flag = False
                            ans.append(w)
                            
        return ans