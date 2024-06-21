# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def traverse(node):
            self.visited.add(node)

            for g in graph[node]:
                if g not in self.visited:
                    self.colors[g] = not self.colors[node]
                    traverse(g)
                else:
                    if self.colors[g] == self.colors[node]:
                        self.isBiPart = False
        
        n = len(graph)

        self.isBiPart, self.visited, self.colors = True, set(), [False for _ in range(n)]

        for i in range(n):
            if i not in self.visited:
                traverse(i)
        
        return self.isBiPart