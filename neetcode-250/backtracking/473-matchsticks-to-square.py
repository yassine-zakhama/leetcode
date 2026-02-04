from typing import List


class Solution:
    # O(4^n), where n is len(matchsticks)
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_len = sum(matchsticks)
        if total_len % 4 != 0:
            return False

        SIDE_LEN = total_len // 4

        # Place large sticks first so bad paths fail early.
        matchsticks.sort(reverse=True)

        if matchsticks[0] > SIDE_LEN:
            return False

        side_len = [0] * 4

        def backtrack(i):
            if i == len(matchsticks):
                return True

            stick = matchsticks[i]
            for side in range(4):
                # Skip identical side states
                if side > 0 and side_len[side] == side_len[side - 1]:
                    continue

                if side_len[side] + stick <= SIDE_LEN:
                    side_len[side] += stick
                    if backtrack(i + 1):
                        return True
                    side_len[side] -= stick

            return False

        return backtrack(0)
