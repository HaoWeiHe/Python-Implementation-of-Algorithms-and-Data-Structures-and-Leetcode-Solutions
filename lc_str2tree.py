# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution(object):
	def str2tree(self, s):

		if not s: return None
		s = "("+s+")" 

		def helper(sub):
			counter = 0
			for idx,ele in enumerate(sub):
				if ele =="(": counter +=1
				if ele ==")": counter -=1
				if counter ==0: 
					return idx+1

		def dfs(sub):

			if not sub : return 
			if sub.count("(")==1: return TreeNode(sub[1:-1])
			sub = sub[1:-1]
			idx = 0
			for i,ele in enumerate(sub):
				if ele =="-" or  ele.isdigit():continue
				idx = i 
				break

			root = TreeNode(sub[:idx])#4
		   # 14(2(3)(1))(6(5))
			sep = helper(sub[idx+1:])
			print(root.val,sep,sub,idx)
			root.left  = dfs(sub[idx+1:idx+sep+1])
			root.right = dfs(sub[idx+sep+1:])
			return root
		
		return dfs(s)

