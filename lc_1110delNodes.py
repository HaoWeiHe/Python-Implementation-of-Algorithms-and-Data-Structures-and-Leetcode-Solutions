class Solution(object):
    def delNodes(self, root, to_delete):

        ans = []
        def dfs(n, is_root = False):
            if not n:
                return None
            if n.val in to_delete:
                dfs(n.right, True)
                dfs(n.left, True)
                return None
            if is_root:
                ans.append(n)
            n.right = dfs(n.right)
            n.left = dfs(n.left)
            return n
        dfs(root, root.val not in to_delete)
        return ans

