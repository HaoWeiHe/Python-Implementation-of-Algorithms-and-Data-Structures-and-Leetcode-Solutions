class Node():
    def __init__(self):
        self.children = defaultdict(Node)
        self.isW = False
class Trie():
    def __init__(self):
        self.root = Node()
        self.root.isW = True
    def insert(self, word):
        node = self.root
        flag = False
        for c in word:
            node = node.children[c]
        node.isW = True
    def check(self, word):
        node = self.root
        
        for c in word:
            if not node.isW:
                return ""
            node = node.children[c]
        return word
class Solution(object):
    def longestWord(self, words):
        """
        ["a","banana","app","appl","ap","apply","apple"]
        
        """
        words.sort()
        
        ans = ""
        trie = Trie()
        for word in words:
            tmp_w = trie.insert(word)
        for w in words:
            tmp_w = trie.check(w)            
            if len(tmp_w) > len(ans):
                ans = tmp_w

        return ans
            
        