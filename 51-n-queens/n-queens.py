class Solution(object):
    def solveNQueens(self, n):
        result = []

        state = [0] * n
        rows, diagonals, anti_diagonals = set(), set(), set()

        def backtrack(col):
            if col == n:
                result.append(state[:])
                return

            for row in range(n if col else int(ceil(n / 2.0))):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                if not (row in rows or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals):
                    rows.add(row)
                    diagonals.add(curr_diagonal)
                    anti_diagonals.add(curr_anti_diagonal)

                    state[col] = row
                    backtrack(col + 1)

                    rows.remove(row)
                    diagonals.remove(curr_diagonal)
                    anti_diagonals.remove(curr_anti_diagonal)


        backtrack(0)

        if not result: return []

        guidelst = ['.' * i + 'Q' + '.' * (n - i - 1) for i in range(n)]

        if n % 2:
            col0_last_num = n // 2
            i = len(result) - 1
            while result[i][0] == col0_last_num:
                state = result[i]
                result[i] = [guidelst[state[j]] for j in range(n)]
                i -= 1
            startPosition = i
        else:
            startPosition = len(result) - 1

        m = n - 1
        for i in range(startPosition, -1, -1):
            state = result[i]
            result.append([guidelst[m - state[j]] for j in range(n)])
            result[i] = [guidelst[state[j]] for j in range(n)]


        return result
        
            