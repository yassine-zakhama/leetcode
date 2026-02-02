from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i_top = stack.pop()[0]
                res[i_top] = i - i_top

            stack.append((i, temp))

        return res
