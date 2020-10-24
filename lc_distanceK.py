# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        ph = dict()
        ch = dict()
        targetNode = None

        def dfs(root,parent):
            if not root: return 
            
            if parent: ph[root]= parent
            if parent not in  ch:
                ch[parent] = []
            if root: ch[parent].append(root)
            dfs(root.right, root)
            dfs(root.left, root)
        
        dfs(root,None)
        level =0
        q = [target]
        seen = set()

        while q:
            if level == K: 
                return([e.val for e in q])
            for _ in range(len(q)):
                top = q.pop(0)

                if top in ph and ph[top] not in seen:
                    q.append(ph[top])
                if top in ch :
                    for e in ch[top]:
                        if e not in seen: 
                            q.append(e)
                seen.add(top)
           
            level +=1
        return []
