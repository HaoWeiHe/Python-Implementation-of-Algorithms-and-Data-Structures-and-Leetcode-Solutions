
import collections

class Solution(object):
	def accountsMerge(self, accounts):
  

		for idx, ac in enumerate(accounts):
			name = ac[0]
			for m in ac[1:]:
				mail2idx[m].add(idx) 
				allmail.add(m)
			mail2name[name] = idx #John, Account0 

		res = []
		for m in allmail:
			tmp = []
			name = ""
			if m not in visited:
				q = collections.deque([m])
				while q:
					top = q.popleft()
					if top in visited: continue
					tmp.append(top)
					visited.add(top)
					# print(top)
					curlst = mail2idx[top]
					for idx in curlst:
						name = accounts[idx][0]
						for a in accounts[idx][1:]:
							if a not in visited:
								q.append(a)
								
			if tmp:	
				tmp.sort()
				tmp = [name] + tmp
				res.append(tmp)

		# print(res)
		return res

accounts = [
["John", "johnsmith@mail.com", "john00@mail.com"], # Account 0
["John", "johnnybravo@mail.com"], # Account 1
["John", "johnsmith@mail.com", "john_newyork@mail.com"],  # Account 2
["Mary", "mary@mail.com"] # Account 3
]
 
accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Solution().accountsMerge(accounts)

