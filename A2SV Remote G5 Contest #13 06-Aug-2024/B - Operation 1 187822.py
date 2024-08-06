# Problem: B - Operation 1 - https://codeforces.com/gym/521860/problem/B

def min_operations(a, m):
    min_ops = a // 2 + a % 2
    
    if min_ops % m == 0:
        return min_ops
    
    next_multiple = ((min_ops // m) + 1) * m
    
    if next_multiple <= a:
        return next_multiple
    else:
        return -1

a, m = map(int, input().split())

result = min_operations(a, m)
print(result)