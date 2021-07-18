class WordDistance(object):

    def __init__(self, wordsDict):
        """
        [[["practice", "makes", "perfect", "coding", "makes"]], 
        practice:0
        makes:[1,4]
        perfect:2
        coding:3
        
        [3,6,8,12]
             ^
        [2,7,9]
             ^
    ans 1  1
        """
        self.d = defaultdict(list)
        for idx, w in enumerate(wordsDict):
            self.d[w].append(idx)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 not in self.d or word2 not in self.d:
            return 
        ans = float('inf')
        i1, i2= 0 ,0
        loc1, loc2 = self.d[word1], self.d[word2]
        while i1 < len(loc1) and i2 < len(loc2):
            ans = min(ans, abs(loc1[i1] - loc2[i2]))
            if loc1[i1] < loc2[i2]:
                i1 += 1
            else:
                i2 += 1
        return ans
                # for i in self.d[word1]:
        #     for j in self.d[word2]:
        #         ans = min(ans, abs(i-j))
        # return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)