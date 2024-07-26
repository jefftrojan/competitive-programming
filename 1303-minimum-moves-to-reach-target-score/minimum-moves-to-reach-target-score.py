class Solution:
    def minMoves(self, target, maxDoubles):
        i, count = 0, 0 

        while i < maxDoubles:
            if target == 1: return count 
            elif target%2 == 0:
                target = target//2 
                count += 1 
                i += 1 
            else:
                target = target-1
                count += 1 

        return count + target - 1

        