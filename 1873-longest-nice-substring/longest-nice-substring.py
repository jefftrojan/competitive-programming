class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        sSet = set(s)
        for i in range(len(s)):
            if s[i].lower() not in sSet or s[i].upper() not in sSet:
                ln1 = self.longestNiceSubstring(s[:i])
                ln2 = self.longestNiceSubstring(s[i+1:])
                return max(ln1, ln2, key=len)
        return s