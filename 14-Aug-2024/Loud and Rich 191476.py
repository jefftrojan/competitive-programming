# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

from collections import defaultdict

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        G = defaultdict(list)
        Gr = defaultdict(list)  # reverse graph
        for a, b in richer:
            G[a].append(b)
            Gr[b].append(a)

        postorder_visit = []
        visited = set()
        for i in range(len(quiet)):
            if i not in visited:
                visited.add(i)
                self.dfs(i, G, postorder_visit, visited)

        topological_order = postorder_visit[::-1]
        
        mins = dict()
        for i in topological_order:
            min_node = i
            min_quiet = quiet[i]
            for from_node in Gr[i]:
                other_quiet, other_node = mins[from_node]
                if other_quiet < min_quiet:
                    min_quiet = other_quiet
                    min_node = other_node
            mins[i] = (min_quiet, min_node)
        
        answer = []
        for i in range(len(quiet)):
            answer.append(mins[i][1])
        return answer

    def dfs(self, node, G, postorder_visit, visited):
        for neighbor in G[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                self.dfs(neighbor, G, postorder_visit, visited)
        postorder_visit.append(node)