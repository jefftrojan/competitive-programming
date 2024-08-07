# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            
            visited[node]=True

            for nei in graph[node]:
                if dfs(nei):
                    return True
            
            visited[node]=False

        for i in range(len(graph)):
            if not dfs(i):
                res.append(i)

        return res
