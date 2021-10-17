class Node():
    def __init__(self, word = None):
        self.children = defaultdict(Node)
        self.word = word
        self.isW = False
        
class Trie():
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.word = word
        node.isW = True
        
    def prefix(self, w):
        ans = []
        node = self.root
        for c in w:
            node = node.children[c]
        
        def dfs(node,):
            
            if node.isW:
                ans.append(node.word)
            
            for c in node.children:
                dfs(node.children[c])
           
            return ans
        dfs(node)        
        return ans
        
            
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        trie = Trie()
       
        for p in products:
            trie.insert(p)
        
        ans = []
        for i in range(1,len(searchWord)+1):
            candidate = trie.prefix(searchWord[:i])
            ans.append(sorted(candidate)[:3])
        return ans
        