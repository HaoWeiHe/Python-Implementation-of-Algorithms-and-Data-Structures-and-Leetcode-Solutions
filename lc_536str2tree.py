# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def str2tree(self, s):
        """
        -4(12(34)(1))(6(5))
        0011122212210112210
          |          |     |
          [idx,     v1      h]
          idx + 1 :v1 v1+2:-1
        -4, (, 12,(,34,),(,1,),),(6,(,5,),)
        if only (, return in the middle
        
        """
        def dfs(s):
            if s.count("(") == 0 :
                if s:
                    return TreeNode(int(s))
                return None
            stk = []

            c = 0 
            root_idx = 0 
            for idx, e in enumerate(s):
                
                if e == "(":
                    c += 1
                    if root_idx == 0:
                        root_idx = idx
                        root = TreeNode(int(s[:root_idx]))
                if e == ")":
                    c -= 1
                if c == 0 and root_idx :
                    stk.append(idx)
            
            v1 = stk.pop(0)
            # print(v1, v2,s,s[:v1])
            # idx + 1 :v1 v1+2:-1
            root.left = dfs(s[root_idx + 1:v1])
            if stk:
                root.right = dfs(s[v1+2:-1])
            return root
        return dfs(s)
            
            
        