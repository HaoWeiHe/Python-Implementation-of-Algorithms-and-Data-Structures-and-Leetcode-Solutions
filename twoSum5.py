# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findTarget(self,root,k):
        if not root:
            return root
		
        dic = dict()
        bfs = [root]
        
        for current_node in bfs:
            
            if not root:
                return False
            
            if k - current_node.val in dic:
                
                return True
            
            dic[current_node.val] = True
            
            if current_node.left : 
                bfs.append(current_node.left)
            if current_node.right: 
                bfs.append(current_node.right)
        return False
        