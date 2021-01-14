class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack  = []
        
        for l in logs:
            fid, func, t = l.split(":")
            fid, t = int(fid), int(t)
            if func == "end":
                t +=1
            
            if stack:
                topid = stack[-1]
                res[topid] += t - pre
            
            if func == "start":
                stack.append(fid)
                
            else:
                stack.pop()
            pre = t
          
        return res