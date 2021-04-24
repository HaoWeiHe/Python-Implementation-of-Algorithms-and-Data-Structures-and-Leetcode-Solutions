"""
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This	is	an", 
   "example  of text",
   "justification.  "
]

1)check if last
2)tmp = [this, is, an, exmple], over -> i -=1
	i = 	1 	2	3	
-> [thisvv, isvv, anv] extend until maxWidth
 	while legnth < maxWidth:
 		i = 0
 		i%=len(tmp)
 		extend " " to tmp[i]
 2) [example of text ] 13
 3) [justification ] and i == len(words), is_last= True
 	if is_last " ".join(tmp)
"""
class Solution(object):
	def fullJustify(self, words, maxWidth):
		"""

		"""
		i, is_last = 0, False
		ans = []
		tmp = []
		tmp_len  = 0

		for i in range(len(words)):
			tmp.append(words[i])

			tmp_len = sum([len(e) for e in tmp]) + len(tmp) - 1
			
			if i == len(words)-1:
				is_last = True
			
			if tmp_len > maxWidth:
				if len(tmp) > 1:
					tmp_len = tmp_len - len(words[i]) - 1
				else:
					tmp_len -= len(words[i])
				tmp.pop()
				opt_idx = 0 
				while tmp_len < maxWidth:

					if len(tmp)>1 :
						opt_idx = opt_idx%(len(tmp)-1)
					else:
						opt_idx = 0
					tmp_len += 1
					tmp[opt_idx]+= " "
					opt_idx += 1
				
				ans.append(" ".join(tmp))
				tmp = [words[i]]

			

			if is_last:
				tmp_len = sum([len(e) for e in tmp]) + len(tmp) - 1
				ans.append(" ".join(tmp) + " " *(maxWidth - tmp_len))
				tmp  = []
				
		
			
		return ans
