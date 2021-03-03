
class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.count = 0
        
class Trie(object):
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
            node.count += 1
        
class Solution(object):
    
    def lcp(self, strs, l,r):
        if l == r: return strs[l]
        mid = (l+r)/2
        lf = self.lcp(strs, l, mid)
        rt = self.lcp(strs, mid+1, r)
        return self.commonpredix(lf,rt)
    
    def commonpredix(self, lf,rt):
        lgth = min(len(lf), len(rt))
        for i in range(lgth):
            if lf[i]!= rt[i]:
                return lf[:i]
        return lf[:lgth]

    def longestCommonPrefix(self, strs):
        """
         ["flower","flow","flight"]
res =      "flower","flo", "fl"
        """
        if not strs:
            return ""
        return self.lcp(strs, 0, len(strs) - 1)
            


    def longestCommonPrefix3(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) ==1:
            return strs[0]
        target = strs[0]
        trie = Trie()
        for w in strs[1:]:
            trie.insert(w)
            
        node = trie.root
        res = 0 
        for c in target:
            if c in node.children and node.children[c].count == len(strs)-1:
                res +=1
                node = node.children[c]
            else:
                break
                
        return target[:res] if res > 0 else ""
        
    def longestCommonPrefix2(self, strs):
        """
         ["flower","flow","flight"]
res =      "flower","flo", "fl"
        """
        if not strs:return ""
        res = strs[0]
        
        for w in strs[1:]:
            length = min(len(w), len(res))
            i = 0 
            res = res[:length]
            while i < length:
                if res[i] != w[i]:
                    res = w[:i]
                    break
                i +=1
                
                
        return res
                
        