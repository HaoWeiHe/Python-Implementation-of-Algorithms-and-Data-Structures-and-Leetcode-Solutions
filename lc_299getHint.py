class Solution(object):
    def getHint(self, secret, guess):
        """
        1123
        0111
         AB
        pos = {1}
       
        i in range(n) i not in pos
        cmpar if 1 in secret
step 1 0
step 2 1, 1 in {} push idx 1 in secret
stp2 3 1, 1 in 2,3
        """
        pos = set()
        candidate = []
        B_num = 0 
        for i in range(min(len(secret), len(guess))):
            if secret[i] == guess[i]:
                pos.add(i)
            else:
                candidate.append(secret[i])
        for i in range(min(len(secret), len(guess))):
            if i in pos:
                continue
            if guess[i] in candidate:
                B_num +=1 
                candidate.remove(guess[i])
        return str(len(pos)) + "A" + str(B_num) + "B"