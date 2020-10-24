class Solution(object):
    
    digit2letters = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }

    def dfs(self,res,digitails,current ):
        if not digitails:
            res.append(current)
            return


        lettes = self.digit2letters[digitails[0]]
        for letter in lettes:
            tmp = current + letter
  
            self.dfs(res, digitails[1:],tmp)

    def letterCombinations(self,digitails):
        if not digitails:
            return []
        res, current = [], ""


        self.dfs(res,digitails,current)
        return res