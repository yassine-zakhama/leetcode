from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            row_sum = 0
            for c in range(cols):
                self.prefix_sum[r][c] = row_sum = row_sum + matrix[r][c]
                if r > 0:
                    self.prefix_sum[r][c] += self.prefix_sum[r - 1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_sum[row2][col2]
        if row1 > 0:
            total -= self.prefix_sum[row1 - 1][col2]
        if col1 > 0:
            total -= self.prefix_sum[row2][col1 - 1]
            if row1 > 0:
                total += self.prefix_sum[row1 - 1][col1 - 1]
        return total
