class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = 'aeiou'
        counts = [0] * len(words)
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                counts[i] = 1
        acc = list(accumulate(counts, initial=0))
        res = []
        for l, r in queries:
            res.append(acc[r + 1] - acc[l])
        return res