from typing import List


class Solution:
    # O(ROWS × COLS × 4^Len(word))
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i_word):
            if i_word == len(word):
                return True
            key = (r, c)
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or key in visited
                or board[r][c] != word[i_word]
            ):
                return False

            visited.add(key)
            new_i = i_word + 1
            if (
                dfs(r + 1, c, new_i)
                or dfs(r - 1, c, new_i)
                or dfs(r, c + 1, new_i)
                or dfs(r, c - 1, new_i)
            ):
                return True
            visited.remove(key)

            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

    # O(ROWS × COLS × 4^Len(word))
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i_word):
            if i_word == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] == ""
                or board[r][c] != word[i_word]
            ):
                return False

            board[r][c] = ""
            new_i = i_word + 1
            if (
                dfs(r + 1, c, new_i)
                or dfs(r - 1, c, new_i)
                or dfs(r, c + 1, new_i)
                or dfs(r, c - 1, new_i)
            ):
                return True
            board[r][c] = word[i_word]

            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
