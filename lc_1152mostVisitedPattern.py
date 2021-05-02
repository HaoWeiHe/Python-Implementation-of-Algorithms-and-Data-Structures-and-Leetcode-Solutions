
import itertools
import collections
class Solution(object):
	def mostVisitedPattern(self, username, timestamp, website):
		"""
		user - [joe] : 1:home 2:about 3:career
				[james]:4:home. 5:cart, 6:maps, 7:home

		combs = ["h a c", ]
		[home, about, career], [home, cart, maps], [home, map, home]..

		"""
		g = collections.defaultdict(list)
		for t, u, w in sorted(zip(timestamp,username, website)):
			g[u].append(w)
		
		combs = []
		for u, w in g.items():
			for e in set(itertools.combinations(w,3)):
				combs += [e]
		C = collections.Counter(combs)
		return sorted(C.items(), key = lambda (x,y): (-y,x))[0][0]
