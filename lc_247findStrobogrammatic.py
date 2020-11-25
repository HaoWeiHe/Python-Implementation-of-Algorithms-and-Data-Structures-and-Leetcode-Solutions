class Solution(object):
    def findStrobogrammatic(self, n):
        """
        even: when n == 0: return ""
        odd : when n ==1: return {0,1,6,8,9}

        101

        """
        middle_lst =  ["0","1","8"]
        pairs = {"1":"1", "6":"9", "9":"6","8":"8","0":"0"}
        self.res = []
        if n == 0:
            return []

        if n == 1:
            return middle_lst


        def dfs(n,odd ):
            res =[]

            if n == 2:
                return [p + pairs[p] for p in pairs]

            if n == 1:
                return [ele for ele in middle_lst]

            return [ p + ele + pairs[p] for p in pairs for ele in  dfs(n-2, odd) ]     

        return [ele for ele in dfs(n,n %2 !=0) if ele[0]!="0"]

