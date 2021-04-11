class Solution(object):
    def topKFrequent(self, words, k):
        """
        K = {"i":2, "love":2 }
        
        """
        C = Counter(words)
        #high fre, and low len
        return [e[0] for e in sorted(C.items(), key= lambda x:(-x[1],x[0]))[:k]]