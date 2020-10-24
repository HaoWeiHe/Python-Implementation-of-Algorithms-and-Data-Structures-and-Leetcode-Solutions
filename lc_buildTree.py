# preorder = [3,9,20,15,7]
# inorder = [9,(3),15,(20),7]


class Solution(object):
	def buildTree(self, preorder, inorder):
		d ={v:k for k,v in enumerate(inorder) }
		self.idx_h = 0
		
		def dfs(lf,rt):
			
			
			if lf ==rt: return 

			root_val = preorder[self.idx_h]
			root = TreeNode(root_val)
			self.idx_h += 1
			index = d[root_val]
			root.left = dfs(lf,index)#subtree[:d[root_val]]) 
			root.right = dfs(index+1, rt)#subtree[d[root_val]+1:])
			
			return root
		
		return dfs(0,len(preorder))

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Solution().buildTree(preorder,inorder)