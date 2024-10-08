# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        adj = defaultdict(set)

        for eq in equations:
            if eq[1:3] == "==":
                u = eq[0]
                v = eq[3]
                adj[u].add(v)
                adj[v].add(u)

        path = set()

        @cache
        def dfs(st, en):
            if st == en:
                return True
            if st in path:
                return False
            path.add(st)
            for ch in adj[st]:
                if dfs(ch, en):
                    return True
            path.remove(st)
            return False

        for eq in equations:
            if eq[1:3] == "==":
                continue
            u = eq[0]
            v = eq[3]
            if dfs(u, v):
                return False

        return True