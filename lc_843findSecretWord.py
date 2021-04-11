# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
   
    def findSecretWord(self, wordlist, master):
        """
        dp[i][0~6]: wordlist[i][n] = lst. the context of lst is the elements whoes have the number n's overlap character whith lst[i]
        
        """
        dp = [[[] for i in range(7)] for _ in range(len(wordlist))]
        for i, e in enumerate(wordlist):
            for j in range(len(wordlist)):
                if i==j:continue
                c =0
                for idx in range(6):
                    if wordlist[i][idx] == wordlist[j][idx]:
                        c +=1
                dp[i][c].append(wordlist[j])
                
        _map = {value:key for key, value in enumerate(wordlist)}
        def getovelap(A,B):
            return list(set(A).intersection(set(B)))
        
        for _ in range(10):
            if len(wordlist) ==0: break
            e = wordlist[0]
            res = master.guess(e)
            _map[e]
            wordlist = getovelap(wordlist,dp[_map[e]][res]) #get the overlap one
            