# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:
    def __init__(self):
        self.d = defaultdict(int)
        self.s = dict()

    def insert(self, key: str, val: int) -> None:
        if(key in self.s):
            val, self.s[key] = val - self.s[key], val
        else:
            self.s[key] = val
        for i in range(1, len(key)+1):
            self.d[key[:i]] += val
        
    def sum(self, prefix: str) -> int:
        return self.d[prefix]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)