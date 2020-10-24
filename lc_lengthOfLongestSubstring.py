
class Solution(object):

	def lengthOfLongestSubstring(self, s):
		tmp = []
		res =  []

		for char in s:
			if char in tmp:
				if len(tmp) > len(res):
					res = tmp
				tmp = tmp[tmp.index(char)+1:]
			tmp.append(char)
	
		if len(tmp) > len(res):
			res = tmp
		return len(res)