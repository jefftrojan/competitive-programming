# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.a = list(range(1,1001))
        heapq.heapify(self.a)

    def popSmallest(self) -> int:
        if len(self.a) > 0:
            return heapq.heappop(self.a)
        return None

    def addBack(self, num: int) -> None:
        if num not in self.a:
            heapq.heappush(self.a, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)