# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)
        flattened_board = [0] * (n * n)
        index = 0
        left_to_right = True
        
        for i in range(n - 1, -1, -1):
            if left_to_right:
                for j in range(n):
                    flattened_board[index] = board[i][j]
                    index += 1
            else:
                for j in range(n - 1, -1, -1):
                    flattened_board[index] = board[i][j]
                    index += 1
            left_to_right = not left_to_right
        
        dist = [-1] * (n * n)
        q = deque([0])
        dist[0] = 0
        
        while q:
            curr = q.popleft()
            if curr == n * n - 1:
                return dist[curr]
            
            for i in range(1, 7):
                next_pos = curr + i
                if next_pos >= n * n:
                    continue
                if flattened_board[next_pos] != -1:
                    next_pos = flattened_board[next_pos] - 1
                if dist[next_pos] == -1:
                    dist[next_pos] = dist[curr] + 1
                    q.append(next_pos)
        
        return -1
