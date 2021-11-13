class Node():
    def __init__(self):
        self.isW = False
        self.children = defaultdict(Node)
        
class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        n = self.root
        for c in word:
            n = n.children[c]
        n.isW = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n  = self.root
        for c in word:
            if c not in n.children:
                return False
            n = n.children[c]

        return True if n.isW else False
    
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        n = self.root
        for c in prefix:
            if c not in n.children:
                return False
            n = n.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)