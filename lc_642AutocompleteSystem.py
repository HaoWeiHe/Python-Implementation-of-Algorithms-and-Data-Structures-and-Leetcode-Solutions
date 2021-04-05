class Node():
    def __init__(self):
        self.children = defaultdict(Node)
        self.isW = False
        self.freq = 0
        self.stn = ""
        
class Trie():
    def __init__(self):
        self.root = Node()
        
    def insert(self, word,freq):
        
        node = self.root
        for c in word:
            node = node.children[c]
        if node.isW:
            node.freq += 1
            
        else:
            node.freq = freq
            node.isW = True
            node.stn = word
        
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie()
        for i, s in enumerate(sentences):
            self.trie.insert(s,times[i])
        self.prex = ""

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":            
            self.trie.insert(self.prex,1)
            self.prex = ""
            return
        
        self.prex += c
        
        prex = self.prex
        trie = self.trie
        
        node = trie.root
        
        res = []
        
        for c in prex:
            node = node.children[c]
        
        
        def dfs(node):
            nxt = []
            if node.isW:
                nxt.append((-node.freq, node.stn))
                
            for c in node.children:
                nxt.extend(dfs(node.children[c]))
            return nxt
        nxt = dfs(node)
        return [e[1] for e in sorted(nxt)[:3]]
        

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)