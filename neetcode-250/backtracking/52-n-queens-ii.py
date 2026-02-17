# O(n!) time, O(n) space
class Solution:
    def totalNQueens(self, n: int) -> int:
        res, taken_cols, pos_diag, neg_diag = [0], set(), set(), set()

        def backtrack(row):
            if row == n:
                res[0] += 1
                return

            for col in range(n):
                pos, neg = row + col, row - col
                if col in taken_cols or pos in pos_diag or neg in neg_diag:
                    continue

                taken_cols.add(col)
                pos_diag.add(pos)
                neg_diag.add(neg)

                backtrack(row + 1)

                neg_diag.remove(neg)
                pos_diag.remove(pos)
                taken_cols.remove(col)

        backtrack(0)
        return res[0]
