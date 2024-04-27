# Problem: B - Mattia Binotto - https://codeforces.com/gym/520098/problem/B

input()

a = b = 0
c = sorted(list(map(int,input().split())))
for i in c:
    if a<=i: a+=i;b+=1
print(b)