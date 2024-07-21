# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

def max_odd_subsequence_sum(n, sequence):
    max_even = 0
    max_odd = float('-inf')
    
    for num in sequence:
        if num % 2 == 0:  
            new_even = max(max_even + num, max_even, num)
            new_odd = max(max_odd + num, max_odd)
        else: 
            new_even = max(max_odd + num, max_even)
            new_odd = max(max_even + num, max_odd, num)
        
        max_even, max_odd = new_even, new_odd
    
    return max_odd

n = int(input())
sequence = list(map(int, input().split()))

result = max_odd_subsequence_sum(n, sequence)
print(result)