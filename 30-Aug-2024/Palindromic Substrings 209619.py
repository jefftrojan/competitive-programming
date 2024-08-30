# Problem: Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            res += self.palindromeCheck(s, i, i)
            res += self.palindromeCheck(s, i, i + 1)
        return res
            
        

    def palindromeCheck(self,s,l,r):
        res=0
        while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
        return res

               
                 
        