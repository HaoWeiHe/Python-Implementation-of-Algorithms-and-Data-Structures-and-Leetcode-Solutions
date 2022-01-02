class Solution(object):
    def removeDuplicates(self, s):
        """
       "abbaca"
          v
    s = [a] cur!=top, append
    if cur == top, pop until empty or != cur 
    
        """
        
        ans = []
        for e in s:#abbaca
            if not ans:
                ans.append(e)
                continue
            if ans[-1] == e:
                while ans and ans[-1] == e:
                    ans.pop()
            else:
                ans.append(e) #[]
                
        return "".join(ans)
        