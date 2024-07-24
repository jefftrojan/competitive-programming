class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        a = len(gas)
        s = 0
        result = 0
        for i in range(a):
            s += gas[i] - cost[i]
            if s < 0:
                s = 0
                result =(i + 1) % a 
        return result