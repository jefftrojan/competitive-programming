# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class UnionFind:
    def __init__(self, n):
        self.parent = [*range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
        
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return a, b
        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
            return b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return a, b


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        min_road = [inf]*(n+1)
        uf = UnionFind(n+1)
        for u, v, dist in roads:
            u, v = uf.union(u, v)
            min_road[u] = min(min_road[u], min_road[v], dist)
        return min_road[uf.find(1)]
  