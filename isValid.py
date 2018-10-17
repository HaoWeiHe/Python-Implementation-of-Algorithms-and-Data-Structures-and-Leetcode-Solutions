class Solution(object):
    def isValid(self, s):
        stack = []

        for c in s:

            if c == '(' or c == '{' or c == '[':
                stack.append(c)

            else:
                if len(stack) == 0:
                    return False
                
                elem = stack.pop()

                if (c == ')' and elem =='(') or (c == '}' and elem == '{') or (c == ']' and elem == '['):
                    pass

                else:
                    return False

        if len(stack) > 0 :
            return False

        return True
