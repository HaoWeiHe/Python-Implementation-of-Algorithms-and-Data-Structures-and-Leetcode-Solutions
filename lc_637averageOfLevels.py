# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = deque([root])
        ans = []
        while q:
            tmp = []
            tmpq = []
            l = len(q)
          
            for _ in range(l):
                top = q.popleft()
                tmp.append(top.val)
                if top.right:
                    q.append(top.right)
                if top.left:
                    q.append(top.left)
           
            
            ans.append(sum(tmp)/float(len(tmp)))
        return ans