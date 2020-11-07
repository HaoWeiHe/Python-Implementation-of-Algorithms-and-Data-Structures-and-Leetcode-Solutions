class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path: 
            return None
        
        s = []
        
        for ele in path.split("/"):
            if ele == ".." :
                if s:
                    s.pop()
            elif ele =="." or not ele:
                continue
            else:
                s.append(ele)
        return "/" + "/".join(s)