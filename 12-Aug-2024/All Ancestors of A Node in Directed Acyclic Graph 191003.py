# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

from collections import deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjList = defaultdict(list)
        in_degree = defaultdict(int)

        for parent, child in edges:
            adjList[parent].append(child)
            in_degree[child] += 1

        queue = deque([node for node in range(n) if node not in in_degree])
        res = [set() for _ in range(n)]
        while queue:
            node = queue.popleft()
            for child in adjList[node]:
                res[child].add(node)
                res[child].update(res[node])
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)
        return [sorted(x) for x in res]