# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        left = max(cookies)
        right = sum(cookies)
        def check(mid):
            def dfs(i):
                if i==len(cookies):
                    return True
                for j in range(len(arr)):
                    if arr[j]+cookies[i]<=mid:
                        arr[j]+=cookies[i]
                        if dfs(i+1):
                            return True
                        arr[j]-=cookies[i]
                return False
            arr = [0 for _ in range(k)]
            return dfs(0)

        while left<=right:
            mid = (left+right)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left