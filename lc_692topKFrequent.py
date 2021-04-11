class Solution(object):
    def topKFrequent3(self, words, k):
        """
   
        """
        C = Counter(words)
        h = [(-f, w) for w,f in C.items()]
        heapq.heapify(h)
        return [heapq.heappop(h)[1] for _ in range(k)]
    def topKFrequent2(self, words, k):
        """
        K = {"i":2, "love":2 }
        
        """
        C = Counter(words)
        #high fre, and low len
        return sorted(C.keys(), key = lambda x: (-C[x],x) )[:k]
    def topKFrequent(self, words, k):
        """
        K = {"i":2, "love":2 }
        
        """
        C = Counter(words)
        #high fre, and low len
        return [e[0] for e in sorted(C.items(), key= lambda x:(-x[1],x[0]))[:k]]