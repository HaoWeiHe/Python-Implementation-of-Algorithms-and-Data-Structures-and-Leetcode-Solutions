
import collections
class Solution(object):
	def minKnightMoves(self, x, y):
		if(x,y)==(0,0): return 0
		dirs = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
		x,y = abs(x),abs(y)
		seen = {(0,0)}
		lenght =0
		q = [(0,0,0)]
		
		for cx,cy,d in q:
			
			for dx, dy in dirs:
				r,c = cx+dx, dy+cy
				if (r,c) not in seen and r > -2 and c > -2:
					if (r,c) == (x,y): return d+1
					q.append((r,c,d+1)) 
					seen.add((r,c))
			
		return -1



  # for i, j, d in open_list:
  #               for di, dj in [(1,2),(2,1),(1,-2),(2,-1),
  #                              (-1,2),(-2,1), (-1,-2),(-2,-1)]:
  #                   r, c = i+di, j+dj
  #                   if (r,c) not in seen and r>-4 and c>-4:
  #                       if (r,c)==(x,y):return d+1
  #                       seen.add((r,c))
  #                       open_list.append((r,c,d+1))
  #       return bfs(0,0,abs(x), abs(y))


x = 2
y = 112
print(Solution().minKnightMoves(x,y))