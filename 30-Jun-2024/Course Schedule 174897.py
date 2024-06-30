# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[a].append(b) 
        
        visiting = set()
        def dfs(a):
            if a in visiting: 
                return False
            if adj[a] == []:
                return True

            visiting.add(a)
            for p in adj[a]:
                if not dfs(p): 
                    return False
            visiting.remove(a)

            adj[a] = [] 
            return True

        for a in range(numCourses):
            if not dfs(a):
                return False
        return True
