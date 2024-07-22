# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

def main():
    n, t = map(int, input().split())
    c = list(map(int, input().split()))
    p = 0

    while p < t - 1:
        p += c[p]

    if p == t - 1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
