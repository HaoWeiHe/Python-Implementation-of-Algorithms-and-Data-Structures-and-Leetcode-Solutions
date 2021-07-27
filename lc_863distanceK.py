# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        3:[5,1]
        5:[6,2]
        2:[7,4]
        1:[0,8]
        """
        self.g = defaultdict(list)
        def dfs(root):
            if not root:
                return 
            if root.right:
                self.g[root.val] += [root.right.val]
                self.g[root.right.val] += [root.val]
            if root.left:
                self.g[root.val]+= [root.left.val]
                self.g[root.left.val]+= [root.val]
            dfs(root.right)
            dfs(root.left)
            
        dfs(root)
        q = deque([])
    
        q.append([target.val,0])
        ans = []
        v = set()
        while q:
            top, level = q.popleft()
            if top in v:
                continue
            v.add(top)
            if level == k :
                # if top != target.val:
                ans.append(top)
                continue
            for ele in self.g[top]:
                q.append([ele, level + 1])
        return ans