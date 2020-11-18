class Solution(object):
    def minAddToMakeValid(self, S):

        counter, res = 0,0
        for e in S:
            if e == "(":
                counter +=1
            else:
                if counter >0:
                    counter -=1

                else:
                    res +=1
        return res + counter

    def minAddToMakeValid2(self, S):
        """
        stack = []
        if stack is empty, and ")" comming, res +=1
        """
        stack = []
        res = 0
        for e in S:
            if e =="(":
                stack.append("(")
           
            else:
                if stack:
                    stack.pop()
                else:
                    res += 1

        return res + len(stack)
S = "()))(("
print(Solution().minAddToMakeValid(S))