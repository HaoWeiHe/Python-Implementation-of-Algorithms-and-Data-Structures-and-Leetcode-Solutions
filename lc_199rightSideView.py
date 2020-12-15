
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res =[]
        
        def dfs(root,lvl):
            if len(res) == lvl:
                res.append(root.val)
            else:
                res[lvl] = root.val
            if root.left:
                dfs(root.left,  lvl+1)
            if root.right:
                dfs(root.right, lvl+1)
                
        dfs(root,0)
        return res

    def rightSideView2(self, root):
        """
        
        """
        if not root:return []
        res =[]
        q = deque([(0,root)])
        while q:
            level, node = q.popleft()
            if node.left:
                q.append((level+1,node.left))
            if node.right:
                q.append((level+1,node.right))
           
            if len(res) == level:
                res.append(node.val)
            else:
                res[level] = node.val
        return res
            