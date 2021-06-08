class Solution(object):
    def simplifyPath(self, path):
        """
        "/home//foo/"
        ["", 'home', "",]
        pth = ["home", "foo"]
        
        /../
        ['..']

        
        "/a/./b/../../c/"
     split:  [a,.,b,..,..,c]
     can  :  [c]
        if . : ignore
        if ..:pop 
        if "": ignore
        
        """
        path_seg = path.split('/')
        candidate = []
        for ele in path_seg:
            if ele == "" or ele == ".":
                continue
            if ele == "..":
                if not candidate:
                    continue
                candidate.pop()
            else:
                candidate.append(ele)
        return "/" + "/".join(candidate)
            
                