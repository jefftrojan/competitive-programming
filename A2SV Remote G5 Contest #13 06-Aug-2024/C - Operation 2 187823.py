# Problem: C - Operation 2 - https://codeforces.com/gym/521860/problem/C

def min_operations(a, b):
    operations = 0
    
    while b > a:
        if b % 2 == 1:
            b += 1
            operations += 1
        else:
            b //= 2
            operations += 1
    
    operations += a - b
    
    return operations

a, b = map(int, input().split())

result = min_operations(a, b)
print(result)