import collections
class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isW = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isW = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for w in word:
            if w not in node.children: return False
            node = node.children[w]
        return node.isW

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for w in prefix:
            if w not in node.children:return False
            node = node.children[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix
class Node():
    def __init__(self):
        self.child = collections.defaultdict(Node)
        
class Trie():
    def __init__(self):
        self.root = Node

        
    def insert(self,word):
        r = self.root
        for c in word:
            r = r.child[c]
            
    def getLeng(self, word):
        res =0
        r = self.root
        for c in word:
            if c not in r.child: return res
            res +=1
            r = r.child[c]
        return res
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
#         build up the tree with first str
#         trace the string[1:] and get the smallest
        if len(strs) <3: return 0
        trie = Trie()
        
        trie.insert(strs[0])
        return max([trie.getLeng(e) for e in strs[1:]])
        
