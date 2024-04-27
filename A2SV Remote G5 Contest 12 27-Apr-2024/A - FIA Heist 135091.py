# Problem: A - FIA Heist - https://codeforces.com/gym/520098/problem/A

def decode_string(s):
    decoded = []
    for char in s:
        if char == '<' and decoded:
            decoded.pop() 
        elif char != '<' and char != '-':
            decoded.append(char) 
    return ''.join(decoded)

intercepted_string = input().strip()

decoded_string = decode_string(intercepted_string)

print(decoded_string)
