class Solution:
    def splitString(self, s: str) -> bool:
        self.res = False
        self.fake = int(s)

        def backtrack(start, prev):
            if start >= len(s) and prev != self.fake:
                self.res = True
                return
            for i in range(start, len(s)):
                num = int(s[start: i+1])
                if num + 1 == prev or prev == -1:
                    backtrack(i+1, num)
        
        backtrack(0,-1)
        return self.res