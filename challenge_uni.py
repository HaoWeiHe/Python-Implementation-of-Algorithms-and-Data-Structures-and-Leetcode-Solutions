import collections
class Unionfind():
    def __init__(self,lst ):
        
        self.parent = [ele for ele in lst]
        self.rank = [0] *len(lst)
    
    def find(self,x,v):
    	if x in v:
    		return None

        if x != self.parent[x]:
            tmp =  self.find(self.parent[x],v + [x])
            if tmp == None:
            	return None
            self.parent[x] = tmp 
        
        return self.parent[x]
            
    def union(self, x, y ):
        px, py = self.find(x,[]), self.find(y,[])
       	if px == None or py == None:
       		return False

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[py] += 1
        return False

tests = [[9, 0, 1, 2, 8, 8, 8, 8, 9, 9], [4,0,1,2,8,8,8,8,8],[3,0,2,2],[1,0], [0,0,2], [0,0,0],[3,0,0,3]]
tans = [True, True,True, False,False, True, True]
class sol():
	def validTree(self, lst):
		uniF = Unionfind(lst)
		for idx, val in enumerate(lst):
			
			if idx == val:
				continue
			if uniF.union(idx, val):
				return False
		
		return len(set(uniF.parent)) == 1


for idx, lst in enumerate(tests):

	print("Right ans?\t{}".format( "Y" if tans[idx] == sol().validTree(lst) else "N"))
	# print(sol().validTree(lst))