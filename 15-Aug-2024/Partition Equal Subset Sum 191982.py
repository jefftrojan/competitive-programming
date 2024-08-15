# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def rec(i,rsum ):
            if(rsum==0): return True
            if(i==len(nums) or rsum < 0): return False 
            elif(self.dp[i][rsum] != -1 ):
                return self.dp[i][rsum]
            self.dp[i][rsum]= rec(i+1,rsum-nums[i]) or rec(i+1,rsum)
            return self.dp[i][rsum]
        
        
        totalsum = sum(nums)
        if(totalsum%2): return False 
        else: 
            self.dp = [ [-1]*((totalsum//2)+1) for _ in range(len(nums))]
            return rec(0,totalsum//2)