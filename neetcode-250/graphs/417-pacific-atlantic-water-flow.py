class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, target):
            if (r, c) in target:
                return
            target.add((r, c))
            for nxt_r, nxt_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (
                    -1 < nxt_r < ROWS
                    and -1 < nxt_c < COLS
                    and heights[r][c] <= heights[nxt_r][nxt_c]
                ):
                    dfs(nxt_r, nxt_c, target)

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS - 1, atlantic)
        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)

        return [[i, j] for i, j in pacific & atlantic]
