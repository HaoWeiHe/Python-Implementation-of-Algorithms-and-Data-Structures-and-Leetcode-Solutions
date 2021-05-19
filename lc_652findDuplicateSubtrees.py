class Solution(object):

    def findDuplicateSubtrees(self, root):
   
        def dfs(root):
            if root is None:
                return "None"
            
            form = hash(str(root.val) + "L" + str(dfs(root.left)) + "R"+str(dfs(root.right)))
            
            forms[form].append(root)
            return form
        forms = defaultdict(list)
        dfs(root)
        return [forms[e][0] for e in forms if len(forms[e]) > 1]


    def findDuplicateSubtrees2(self, root):
   
        def dfs(root):
            if root is None:
                return "None"
            
            form = str(root.val) + "L" + str(dfs(root.left)) + "R"+str(dfs(root.right))
            
            forms[form].append(root)
            return form
        forms = defaultdict(list)
        dfs(root)
        return [forms[e][0] for e in forms if len(forms[e]) > 1]



