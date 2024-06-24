class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        Bomb = tuple[int, int, int]
        T = Hashable
        Graph = Mapping[T, Collection[T]]

        def in_range(b1: Bomb, b2: Bomb) -> bool:
            return (b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2 <= b1[2] ** 2

        def connections(graph: Graph, src: T, seen: set[T]) -> int:
            return seen.add(src) or 1 + sum(connections(graph, x, seen) for x in graph[src] if x not in seen)

        g = {i: tuple(j for j, b2 in enumerate(bombs) if in_range(b1, b2)) for i, b1 in enumerate(bombs)}
        return max(connections(g, x, set()) for x in g)
