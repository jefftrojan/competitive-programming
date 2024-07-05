from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m=len(maze)
        n=len(maze[0])
        def valid(row,col):
            return 0<=row<m and 0<=col<n
        seen=set()
        seen.add((entrance[0],entrance[1]))
        que=deque()
        que.append((entrance[0],entrance[1],0))
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        while que:
            row,col,steps=que.popleft()
            if maze[row][col]!="+" and [row,col]!=entrance:
                if row==0 or col==n-1 or col==0 or row==m-1:
                    return steps
            for dx,dy in directions:
                new_row,new_col=row+dy,col+dx
                if valid(new_row,new_col) and maze[new_row][new_col]!="+":
                   if (new_row,new_col) not in seen:
                       seen.add((new_row,new_col))
                       que.append((new_row,new_col,steps+1))

        return -1