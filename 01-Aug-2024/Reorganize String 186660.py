# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:
        n=len(s)
        freq=dict()
        for ch in s:
            freq[ch]=1+freq.get(ch,0)

        hp=[(-v,k) for k,v in freq.items()]  
        heapify(hp)

        i=0
        ans=[""]*n  
        while hp:
            v,k=heappop(hp)
            v=-v
            if 2*v-1>n:
                return ""

            for _ in range(v):
                ans[i]=k
                i=i+2 if i+2<n else 1  

        return "".join(ans)          