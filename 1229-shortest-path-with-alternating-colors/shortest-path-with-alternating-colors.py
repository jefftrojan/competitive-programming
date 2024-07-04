class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        lst=[-1]*n
        grid=[[] for i in range(n)]
        vr=[-1]*n
        vb=[-1]*n
        for i,j in redEdges:
            grid[i].append((j,True))
        
        for i,j in blueEdges:
            grid[i].append((j,False))

        queue=[(0,0,True),(0,0,False)]
        vb[0]=1
        vr[0]=1
        while queue:
            d,x,flg=queue.pop(0)
            if lst[x]==-1:
                lst[x]=d
            for to,fg2 in grid[x]:
                if flg!=fg2:
                    if (fg2==False and vb[to]==-1):
                        queue.append((d+1,to,fg2))
                        vb[to]=1
                    elif (fg2==True and vr[to]==-1):
                        queue.append((d+1,to,fg2))
                        vr[to]=1
        return lst
            