class Solution(object):
    def asteroidCollision(self, A):
        """
        if stack[-1] < 0 or e > 0, keep treaking
        if e < 0 and stack[-1] > 0:
            check stack[-1]
        """
        stack = []

        for e in A:
            while stack and e < 0 < stack[-1]:
                if stack[-1] < -e:
                    stack.pop()
                    continue
                elif stack[-1] == -e:
                    stack.pop()
                break   
            else:
                stack.append(e)
                    
        return stack
