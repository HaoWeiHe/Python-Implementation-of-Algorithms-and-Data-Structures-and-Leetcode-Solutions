
class Solution(object):


		def reconstructQueue(self, people):

			def my_cmp(p1,p2):
				return cmp(p2[1],p1[1]) if p1[0]==p2[0] else cmp(p1[0],p2[0])
			
			res = []

			people.sort(cmp=my_cmp,reverse=False)
			
			people_extend = list()
			
			for tup in people:
				tup.append(tup[1])
				
			

			def func(people,res):
				
				for tup in people:
					
					if tup[1] == 0:
						people.remove(tup)

						res.append([tup[0],tup[2]])
					

						for inner_tup in people:
							if inner_tup[0] <= tup[0]:
								inner_tup[1] -= 1
								
						
						break				
					
				people.sort(cmp=my_cmp,reverse=False)
				return people, res
			
			while len(people) > 1:
				people,res = func(people,res)

			for tup in people:
				res.append([tup[0],tup[2]])
			
			return res
