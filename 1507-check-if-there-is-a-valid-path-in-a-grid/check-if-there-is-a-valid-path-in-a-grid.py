class Solution(object):
	def hasValidPath(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: bool
		"""
		street = {1:['l','r'],
		 2:['u','d'],
		 3:['l','d'],
		 4:['r','d'],
		 5:['u','l'],
		 6:['u','r']}

		visit = set()
		rows, cols = len(grid), len(grid[0])

		stack = []
		stack.append((0,0))

		while stack:    
			i, j = stack.pop()        
			if (i, j) not in visit:
				d1, d2 = street[grid[i][j]]
				for d in [d1, d2]:
					if d == 'u' and 0<=i-1<rows and (i-1,j) not in visit and 'd' in street[grid[i-1][j]]:
						stack.append((i-1,j))
					elif d == 'd' and 0<=i+1<rows and (i+1,j) not in visit and 'u' in street[grid[i+1][j]]:
						stack.append((i+1,j))
					elif d == 'l' and 0<=j-1<cols and (i,j-1) not in visit and 'r' in street[grid[i][j-1]]:
						stack.append((i,j-1))
					elif d == 'r' and 0<=j+1<cols and (i,j+1) not in visit and 'l' in street[grid[i][j+1]]:
						stack.append((i,j+1))
			visit.add((i,j))
			if i+1 == rows and j+1 == cols:
				return True
		return False