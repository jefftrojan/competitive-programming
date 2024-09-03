# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    import math
    def maxProduct(self, words: List[str]) -> int:
        def get_code(s) :
            code = 0
            for i in s :
                k = ord(i) - 97 
                code |= 1 << k 
                
            return code
        h = {}
        for word in words :
            h[word] = get_code(word)
            
        m = -math.inf        
        for i in range(len(words)) :
            for j in range(i + 1 , len(words)) :
                if h[words[i]] & h[words[j]] == 0 :
                    m = max(m , len(words[i] ) * len(words[j]))
                    
                    
        return m if m > 0 else 0
            