from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def do_mark(r, c, new_mark):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] == "X"
                or board[r][c] == new_mark
            ):
                return
            board[r][c] = new_mark
            do_mark(r + 1, c, new_mark)
            do_mark(r - 1, c, new_mark)
            do_mark(r, c + 1, new_mark)
            do_mark(r, c - 1, new_mark)

        def mark_edges(new_mark):
            for c in range(COLS):
                do_mark(0, c, new_mark)
                do_mark(ROWS - 1, c, new_mark)
            for i in range(ROWS):
                do_mark(i, 0, new_mark)
                do_mark(i, COLS - 1, new_mark)

        mark_edges("Y")

        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if board[r][c] == "O":
                    board[r][c] = "X"

        mark_edges("O")
