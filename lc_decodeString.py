# class Solution(object):
# 	def decodeString(self, s):
# 		"""
# 		:type s: str
# 		:rtype: str
# 		"""
# 		"3[a]2[bc]"
# 		"3[a2[c]]"
# 		# nums = [3,2] queue
# 		nums, stack, s =[],[], list(s)
# 		tmps = s[::]
# 		cur_num = []

# 		for e in tmps:
# 			if e.isdigit():
# 				cur_num.append(e)
# 			else:
# 				if e =="[":
# 					nums.append(int("".join(cur_num)))
# 					cur_num = []
# 				if e =="]":
# 					top = stack.pop()
# 					pre = ""
# 					while top!="[":
# 						pre = top + pre 
# 						top = stack.pop()
# 					stack.append(nums.pop()*pre)
# 				else:
# 					stack.append(e)

# 		return ''.join(stack)
class Solution(object):
	def decodeString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		

s = "abc3[cd]xyz"#"2[abc]3[cd]ef"
print(Solution().decodeString(s))

