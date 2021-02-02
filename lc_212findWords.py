
import collections
class Node():
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False
        self.w = ""
class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self,word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True
        node.w = word
    def pruning(self, word):
        node = self.root
        parent = None
        while True:
            for c in word:
                parent = node
                node = node.children[c]
                
            if not node.children and word:
                del parent.children[word[-1]]
                word = word[:-1]
            else:
                break
           
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
        self.visted_word = set()
        def dfs(node,x,y,v):
         
            if not node:
                return 

            if board[x][y] not in node.children:
                return 
            
            node = node.children[board[x][y]]
            if node.isWord:
                self.res.append(node.w)
                trie.pruning(node.w)

            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx, ny = dx + x, dy + y 
                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in v :
                    dfs(node,nx,ny,v + [(nx,ny)])
                        

        m,n = len(board), len(board[0])           
        root = trie.root
        
        for i in range(m):
            for j in range(n):
                dfs(root, i,j,[(i,j)])

        return list(set(self.res))
