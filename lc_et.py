class ET():
	def __init__(self,val):
		self.val = val
		self.right = None
		self.left =None

def isOperater(c):
	return c in ["+","-","*","/"]

def inorder(r):
	if r:
		inorder(r.left)
		print(r.val),
		inorder(r.right)

def buildtree(postfix):
	s  = []
	for c in postfix:
		if not isOperater(c):
			s.append(ET(c))
		else:
			rt = s.pop()
			lf = s.pop()
			p = ET(c)
			p.right = rt
			p.left = lf
			s.append(p)
	return s.pop()
postfix = "ab+ef*g*-"
r = buildtree(postfix)
inorder(r)