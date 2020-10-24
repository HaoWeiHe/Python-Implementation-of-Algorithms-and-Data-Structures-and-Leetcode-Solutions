
class Solution(object):

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        #depth, length
        
        stack = [(-1,0)]

        lengthSum = 0
        res = 0
        dirLst = input.split('\n')


        for item in dirLst:
            
            #if num(\t) < stackLevel then pop
            #else push until num(\t) 

            topDepth, topLength = stack[-1]
            n_p = item.count("\t")
            name = item.replace("\t","")

            while topDepth >= n_p :
                stack.pop()
                lengthSum -= topLength
                topDepth, topLength = stack[-1]
            

            lengthSum = len(name) + (n_p > 0) + topLength

            stack.append((n_p, lengthSum))

            if "." in item:
                res = max(res, lengthSum)
            
        return res




