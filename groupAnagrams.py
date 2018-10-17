
class Solution(object):
	def groupAnagrams(self, strs):
		dic = dict()
		lst = list(tuple())
		for elem in strs:
			sortedelem  = ''.join(sorted(elem))
			if not sortedelem in dic:
				dic[sortedelem] = list()

			dic[sortedelem].append(elem)

		
		res = []

		for key in dic:
			res.append(dic[key])
		return res