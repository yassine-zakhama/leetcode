from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack, i = [], 0
        while i < len(asteroids):
            ast = asteroids[i]
            if ast > 0 or not stack or stack[-1] < 0:
                stack.append(ast)
                i += 1
                continue

            if stack[-1] == abs(ast):
                stack.pop()
                i += 1
            elif stack[-1] > abs(ast):
                i += 1
            else:
                stack.pop()

        return stack
