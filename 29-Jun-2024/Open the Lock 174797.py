# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        if "0000" in deadends:
            return -1
        q=deque([("0000",0)])
        visited=set()
        while q:
            cand,steps=q.popleft()
            if cand==target:
                return steps
            for i in range(4):
                for digit in [((int(cand[i])+1)%10),((int(cand[i])-1)%10)]:
                    nx=cand[:i]+str(digit)+cand[1+i:]
                    if nx not in deadends and nx not in visited:
                        visited.add(nx)
                        q.append((nx,steps+1))
        return -1                       