
class RandomizedSet(object):

	def __init__(self):
		"""
		[1,7,3,9]
	{1:0, 7:1, 3:2, 9:3}
	insert: update d and append to list
	del x: replace tail to idx of x, pop list()
	random:
		"""
		self.lst = []
		self.d = {}
		

	def insert(self, val):
		
		if val in self.d: return 0
		
		self.d[val] = len(self.lst)
		self.lst.append(val)
		return 1
	
	def remove(self, val):
		"""
		Removes a value from the set. Returns true if the set contained the specified element.
		:type val: int
		:rtype: bool
		"""
		if val not in self.d: return 0  
	   	if self.d[val] == len(self.lst) -1:
	   		self.lst.pop()
	   		del self.d[val]
	   		return 1
		target_idx = self.d[val] #[1,8,7,9] remove: 8 target_idx = 1  target -> [1,9,7] ,update d[9] = 1
		del self.d[val]
		swap = self.lst[-1]#swap = 9 ->  
		self.lst[target_idx] = swap
		self.d[swap] = target_idx
		self.lst.pop()
		
		return 1
	
	def getRandom(self):
		"""
		Get a random element from the set.
		:rtype: int
		"""
		return random.choice(self.lst)
		


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()