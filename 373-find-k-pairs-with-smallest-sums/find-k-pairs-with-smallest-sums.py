from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        heap = []
        heappush(heap,(0,0,0))
        visited = set([(0,0)])
        for _ in range(k):
            if heap:
                _ , ix1, ix2 = heappop(heap)
                ans.append([nums1[ix1],nums2[ix2]])

                for new_ix1 , new_ix2 in [[ix1+1,ix2],[ix1,ix2+1]]:
                    if 0<=new_ix1 < len(nums1) and 0<=new_ix2<len(nums2)  and (new_ix1,new_ix2) not in visited:
                        total_sum = nums1[new_ix1] + nums2[new_ix2]
                        heappush(heap,(total_sum,new_ix1,new_ix2) )
                        visited.add((new_ix1,new_ix2))
        return ans