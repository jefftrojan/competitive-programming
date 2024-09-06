# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(u,v):
            if u in visited:
                return False
            if u == v:
                return True
            
            visited.add(u)
            
            for i in graph[u]:
                if dfs(i, v):
                    return True
            return False
        
        
        n = len(edges)
        graph = defaultdict(list)
        
        
        ans = []
        for u, v in edges:
            visited = set()
            if dfs(u, v):
                ans = [u,v]
            graph[u].append(v)
            graph[v].append(u)
        return ans