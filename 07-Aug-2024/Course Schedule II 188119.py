# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def dfs(self,node,edges,vis,inPath) :
        if inPath[node] :
            return True
        if vis[node] :
            return False
        
        vis[node] = 1
        inPath[node] = 1

        for neigh in edges[node] :

            if self.dfs(neigh,edges,vis,inPath) :
                return True

        inPath[node] = 0
        return False
    def isCyclic(self,edges, v):

        adj = [[] for i in range(v)]
        vis= [0] * v
        inPath = [0] * v
        for edge in edges:
            adj[edge[0]].append(edge[1])
        for node in range(v) :
            if not(vis[node]) :
                if self.dfs(node,adj,vis,inPath) :
                    return True
        return False
    def toposort(self,adj,V) :
        vis = [0 for i in range(V)]
        st = []

        def dfs(node) :
            vis[node] = 1
            for neigh in adj[node] :
                if not(vis[neigh]) :
                    dfs(neigh)
            st.append(node)

        for node in range(V) :
            if not(vis[node]) :
                dfs(node)
        
        return st
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        V = numCourses
        adj = [[] for i in range(V)]
        for edge in prerequisites :
            adj[edge[0]].append(edge[1])
        isCyclic = self.isCyclic(prerequisites,V)
        if isCyclic :
            return []
        res = self.toposort(adj,V)
        return res 