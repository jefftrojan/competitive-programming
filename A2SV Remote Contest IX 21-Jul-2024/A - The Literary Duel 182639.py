# Problem: A - The Literary Duel - https://codeforces.com/gym/515369/problem/A

def calculate_scores(n, books):
    hermione_score = 0
    harry_score = 0
    left = 0
    right = n - 1
    hermione_turn = True

    while left <= right:
        if books[left] > books[right]:
            chosen = books[left]
            left += 1
        else:
            chosen = books[right]
            right -= 1

        if hermione_turn:
            hermione_score += chosen
        else:
            harry_score += chosen

        hermione_turn = not hermione_turn

    return hermione_score, harry_score

n = int(input())
books = list(map(int, input().split()))

hermione_final, harry_final = calculate_scores(n, books)

print(f"{hermione_final} {harry_final}")