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
        #dp[i][c]
        dp = [[[] for i in range(7)] for _ in range(len(wordlist))]
        for i, e in enumerate(wordlist):
            for j in range(len(wordlist)):
                if i==j:continue
                c =0
                for idx in range(6):
                    if wordlist[i][idx] == wordlist[j][idx]:
                        c +=1
                dp[i][c].append(wordlist[j])
                
        _map = {w:idx for idx, w in enumerate(wordlist)}
        def getovelap(A,B):
            return list(set(A).intersection(set(B)))
        
        res = 0 
        while res < 6:   
            if len(wordlist) ==0: break
            tmp = ""
            _mn,cans = float('inf'), None
            for ele in wordlist:
                tmp = max([ len(dp[_map[e]][i]) for i in range(7)])
                if  tmp < _mn:
                    _mn = tmp
                    cans = ele
            e = cans
            res = master.guess(e)
            
            wordlist = getovelap(wordlist,dp[_map[e]][res]) #get the overlap one
            