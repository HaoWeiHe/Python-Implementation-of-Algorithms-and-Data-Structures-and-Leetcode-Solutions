# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append(None)
                return None
            
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
        

    def deserialize(self, lst):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
    
        def dfs(lst):
            if  lst[0] is None :
                lst.pop(0)
                return None
            root = TreeNode(lst.pop(0))
            root.left = dfs(lst)
            root.right = dfs(lst)
            return root
        return dfs(lst)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))