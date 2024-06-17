# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        first = [i[0] for i in trust]
        case1 = (n*(n+1))//2 - sum(set(first))
        if case1 == 0:
            return -1
        else:
            for j in range(1,n+1):
                if j == case1:
                    continue
                elif [j,case1] not in trust:
                    return -1
            return case1