class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        graph=defaultdict(set)
        for routes_id,stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(routes_id)
                
        queue=deque([(source,0)])
        seen_stops=set([source])
        seen_routes=set()
        while queue:
            stop,new_changes=queue.popleft()
            
            if stop==target:
                return new_changes
            
            for routes_id in graph[stop]:
                if routes_id not in seen_routes:
                    seen_routes.add(routes_id)
                    
                    for stop in routes[routes_id]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            queue.append((stop,new_changes+1))
                            
        return -1                   