from collections import defaultdict

class Node():
    def __init__(self, word = None):
        self.children = defaultdict(Node)
        self.suggest = []
        
class Trie():
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
            if len(node.suggest) < 3:
                node.suggest.append(word)
              
class Solution(object):
    def suggestedProducts(self, products, searchWord):

        trie = Trie()
        products.sort()
        
        for p in products:
            trie.insert(p)
        
        ans = []
        node = trie.root
        for c in searchWord:
            node = node.children[c]
            ans.append(node.suggest)
            
        return ans
