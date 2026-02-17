# O(n!) time, O(n^2) space
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]

        res, taken_cols, pos_diag, neg_diag = [], set(), set(), set()

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                pos, neg = row + col, row - col
                if col in taken_cols or pos in pos_diag or neg in neg_diag:
                    continue

                board[row][col] = "Q"
                taken_cols.add(col)
                pos_diag.add(pos)
                neg_diag.add(neg)

                backtrack(row + 1)

                neg_diag.remove(neg)
                pos_diag.remove(pos)
                taken_cols.remove(col)
                board[row][col] = "."

        backtrack(0)
        return res
