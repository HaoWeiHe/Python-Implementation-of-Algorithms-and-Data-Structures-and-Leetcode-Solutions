import collections
class Solution(object):
	def lengthLongestPath(self, input):
		res = 0
		record = {0:0}
		
		for ele in input.split("\n"):
			depth = ele.count("\t")
			name = ele.lstrip("\t")
			if "." in name:
				res = max(res, record[depth] + len(name))
			else:
				record[depth+1] = record[depth] + len(name) + 1
		return res

input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir222\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(Solution().lengthLongestPath(input))