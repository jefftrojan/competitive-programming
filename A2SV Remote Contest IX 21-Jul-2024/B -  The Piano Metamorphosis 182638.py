# Problem: B -  The Piano Metamorphosis - https://codeforces.com/gym/515369/problem/B

def find_minimum_height_planks(n, k, heights):
    if k > n:
        return 0 

    current_sum = sum(heights[:k])
    min_sum = current_sum
    min_index = 0

    for i in range(1, n - k + 1):
        current_sum = current_sum - heights[i-1] + heights[i+k-1]
        if current_sum < min_sum:
            min_sum = current_sum
            min_index = i

    return min_index + 1 

n, k = map(int, input().split())
heights = list(map(int, input().split()))
result = find_minimum_height_planks(n, k, heights)
print(result)