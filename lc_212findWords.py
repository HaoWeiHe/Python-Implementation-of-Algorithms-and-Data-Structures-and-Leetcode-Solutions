
import collections
class Node():
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False
        self.w = Node
class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self,word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True
        node.w = word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for w in words:
            trie.insert(w)

        self.res = []

        def dfs(node,x,y,v):
            if not node:
                return 
            if board[x][y] not in node.children:
                return 
            node = node.children[board[x][y]]
            if node.isWord:
                self.res.append(node.w)

            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx, ny = dx + x, dy + y 
                if 0 <= nx < m and 0 <= ny < n and (x,y) not in v :
                    dfs(node,nx,ny,v + [(x,y)])
                        

        m,n = len(board), len(board[0])           
        root = trie.root
        
        for i in range(m):
            for j in range(n):
                dfs(root, i,j,[])

        return list(set(self.res))

    def findWords2(self, board, words):
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
