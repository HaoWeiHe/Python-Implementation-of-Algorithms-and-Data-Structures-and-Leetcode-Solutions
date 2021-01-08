class Node():
    def __init__(self, val = None):
        self.val = val
        self.children = collections.defaultdict(Node)
        self.isWord = False
class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True
    
   
    def search(self, word):
            
        node = self.root
        for idx, c in enumerate(word):
            if c ==".":
                return any([self.search(word[:idx] + e + word[idx+1:]) for e in node.children])
            else:
                if c not in node.children:
                    return False
                node = node.children[c]
            
        return node.isWord
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)