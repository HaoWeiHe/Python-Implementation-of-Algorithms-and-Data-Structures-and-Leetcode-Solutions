class Solution(object):
    def addBoldTag(self, s, dict):
        """
         ["aaa","aab","bc"]
         "aaabbcc"
          0123456
         [(0,4], ]
         top[1] <= idx-length, update to idx
         
         ["abc","123"]
         "abcxyz123"
          012345678
         [(0,3) (idx-len, idx)]
         
        """
        i = 0
        stack = []
        while i <=len(s):
           
            for w in dict:
                if len(w) > i : continue
                start = float('inf')
                end = float('-inf')
                if s[i-len(w):i] ==w:
                    # [(37, 364), (94, 498), (367, 620)]
                    while stack and stack[-1][1] >= i - len(w):
                        
                        start,end  = stack.pop()

                    stack.append((min(start, i - len(w)), i))
                    i = max(i,end-1)
 
            
            i += 1
        print(stack)
        """
        #[0,3], [6,9]
         i:0  +  i: 3, update i = 3+ 1 =4
        i = 0
        top = stack.pop(0)
        ans = ans + s[top[0]:top[1]]
        i = top[1]+1
        """
        i = 0 
        ans = ""
        while stack:
            start, end = stack.pop(0)
            ans = ans + s[i: start] + "<b>" +s[start:end] + "</b>" 
           
            i = end
        ans = ans + s[i:]
        return ans
