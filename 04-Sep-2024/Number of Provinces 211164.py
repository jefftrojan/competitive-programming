# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)  #1
        visited = [False]*n  #2
        count = 0  #3
        
        if not M:  #4
            return 0  #5
        
        def dfs(u):  #6
            for v in range(n):  #7
                if M[u][v] == 1 and visited[v] == False:  #8
                    visited[v] = True  #9
                    dfs(v)  #10
        
        
        for idx in range(n): #11
            if visited[idx] == False: #12
                count += 1 #13
                visited[idx] == True #14
                dfs(idx) #15
        
        return count #16