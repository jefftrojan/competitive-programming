class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = {"T":0,"F":0}
        i = 0
        ans = 0
        for j in range(len(answerKey)):
            count[answerKey[j]] += 1
            while count["T"] > k and count["F"] > k:
                count[answerKey[i]] -= 1
                i += 1
            ans = max(ans,j-i + 1)
        return ans
            
                