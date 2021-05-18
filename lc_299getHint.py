from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        [1,2,3,1]
        [0,1,1,1]
               v 
        {1:2, 2:1,3:1} 0A0B
        {1:1, 2:1,3:1} 0A1B
        {1:0, 2:1,3:1} 0A2B
        {1:0, 2:1,3:1} 1A1B
        
        """
        c = Counter(secret)
        A,B = 0,0
        for i, v in enumerate(guess):
            if v not in c:
                continue
            if secret[i] == v:
                if c[v] == 0:
                    B -= 1
                else:
                    c[v] -= 1
                A += 1
            else: 
                if c[v] ==0:
                    continue  
                c[v]-= 1
                B += 1
        return str(A) + "A" + str(B) + "B"
