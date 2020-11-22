class Solution(object):
    def removeDuplicates(self, S):
        """
        
        use stack
        """
        stack = []
        
        for e in S:             
            if stack and e == stack[-1]:
                stack.pop()
            else:
                stack.append(e)
        
        return "".join(stack)
                
            
