from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        seen = set()

        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]


        def divide(a, b):
            if a == b:
                return 1.00000

            seen.add(a)
            for key, value in graph[a].items():
                if key in seen:
                    continue

                res = divide(key, b)
                if res > 0:
                    return float(res * value)
            return -1.000

        ans = []
        for q in queries:
            a, b = q[0], q[1]

            if a not in graph or b not in graph:
                ans.append(-1.000)
                continue

            seen = set()
            ans.append(divide(a, b))

        return ans