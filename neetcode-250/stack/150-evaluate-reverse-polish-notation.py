from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands, stack = set(["+", "-", "*", "/"]), []
        for t in tokens:
            if t not in operands:
                stack.append(int(t))
                continue

            b, a = stack.pop(), stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))

        return stack[-1]
