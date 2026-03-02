class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 and c == 0:
                    continue
                elif obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                    continue

                if r > 0:
                    obstacleGrid[r][c] += obstacleGrid[r - 1][c]
                if c > 0:
                    obstacleGrid[r][c] += obstacleGrid[r][c - 1]

        return obstacleGrid[ROWS - 1][COLS - 1]
