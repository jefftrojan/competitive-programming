# Problem: A - Rudolph and Cut the Rope  - https://codeforces.com/gym/533316/problem/A

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        k = int(data[index])
        index += 1
        cnt = 0
        
        for _ in range(k):
            a = int(data[index])
            b = int(data[index + 1])
            index += 2
            if a - b > 0:
                cnt += 1
        
        results.append(cnt)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
