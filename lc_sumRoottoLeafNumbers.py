# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def __init__(self):
		self.s = ""
		self.total = 0
    
	def sumNumbers(self, root):
		if not root:
			return 0

		self.sumNumbersHelper(root)

		return self.total

	def sumNumbersHelper(self,root):


		if not root and len(self.s) == 1 :
				return self.total
		self.s += str(root.val)    


		if ((not root.left) and (not root.right)):
			self.total += int(self.s)
			self.s = self.s[:-1] 
			return 

		self.sumNumbers(root.left)
		self.sumNumbers(root.right)

		self.s = self.s[:-1] 