# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = [False] * N

        def visit(room):
            visited[room] = True
            for key in rooms[room]:
                if not visited[key]:
                    visit(key)
        visit(0)
        return all(visited
        )
