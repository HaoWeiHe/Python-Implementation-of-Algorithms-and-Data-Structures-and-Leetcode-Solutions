class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(set)
        
        def generalFormat(w):
            for i in range(len(w)):
                yield w[:i] + "#" + w[i+1:]
                
        for w in wordList: 
            for ele in generalFormat(w):
                d[ele].add(w)

        q = deque([[beginWord,[beginWord]]])
        shortest_path_length = float("inf") 
        ans = []
        v = {}
        
        while q:
            cur_w, history = q.popleft()   
            if cur_w in v and v[cur_w] < len(history):
                continue
            v[cur_w] = len(history)
            if cur_w == endWord :
                shortest_path_length = min(shortest_path_length, len(history))
                ans.append(history )
        
            for ele in generalFormat(cur_w):
                for nextW in d[ele]:
                    q.append([nextW, history + [nextW]])
        return ans