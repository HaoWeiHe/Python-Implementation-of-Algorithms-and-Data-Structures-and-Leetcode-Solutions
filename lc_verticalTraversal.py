# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        d = collections.defaultdict(list)
     
        if not root:return []
        q = deque([(root,0,0)])
        
        while q :
            root, lvl, high = q.popleft()
            
            d[lvl].append((root.val, high))
            
            if root.left:
                q.append((root.left, lvl -1,high -1))
            if root.right :
                q.append((root.right, lvl+1,high -1))
        res =[]
        for k in sorted(d.keys()):
            
            tmp = sorted(d[k], key = lambda (v,h):(-h,v))
            res.append([e[0] for e in tmp])
       
        return res#[e[1] for e in sorted_lst]



