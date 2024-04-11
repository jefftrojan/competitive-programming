class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        i = 0
        
        while i < len(chars):
            j = i + 1
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            chars[idx] = chars[i]
            idx += 1
            if j - i > 1:
                count_str = str(j - i)
                chars[idx:idx+len(count_str)] = count_str
                idx += len(count_str)

            i = j
        del chars[idx:]
        return len(chars)