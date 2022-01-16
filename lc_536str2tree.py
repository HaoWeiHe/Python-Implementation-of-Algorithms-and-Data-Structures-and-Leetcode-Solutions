# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def str2tree2(self, s):
        """
        4(2(3)(1))(6(5))
                    ^
         open: construct new tree, root = val, idx _next_to_val
         close: return and return idx + 1
        """
        def get_idx_val(idx):
            flag = 1
            num = 0 
            while idx < len(s) and (s[idx].isdigit() or s[idx] == "-") :
                if s[idx] == "-":
                    flag = -1
                else:
                    num = num*10 + int(s[idx])
                idx += 1
           
            return num * flag, idx
        
        def dfs(idx):
            if idx == len(s):
                return None, idx
            val, idx = get_idx_val(idx)
            root = TreeNode(val)
            if idx < len(s) and s[idx] == "(":
                root.left, idx = dfs(idx + 1)
                
            if root.left and idx < len(s) and s[idx] == "(":
                root.right, idx = dfs(idx + 1)
            return root, idx if idx < len(s) and s[idx] == "(" else idx + 1
        return dfs(0)[0]
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
         
            root.left = dfs(s[root_idx + 1:v1])
            if stk:
                root.right = dfs(s[v1+2:-1])
            return root
        return dfs(s)
            
            
        