class Solution(object):
    def countBinarySubstrings(self, s):
        """
        0, 0, 1, 1, 0, 0, 0,1,1
                    ^
     [1,0]
         [2,0]
             [2,1] -> ans  = 1
                [2,2] -> ans = 2
                   [1,2]
                      [2,2]
       
      
         if not == pre, clean to 1
         
        """
        if not s:return 0
        count = [float('-inf'),float('-inf')] 
        count[int(s[0])] = 1 #[2,2]
        pre = int(s[0])
        ans = 0 
        for e in s[1:]:
            e = int(e)
            if e != pre:
                count[e] = 1
            else:
                count[e] += 1
            if count[e] <= count[~e]:
                ans +=1 
            pre = e
        return ans