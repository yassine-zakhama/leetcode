from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (-1, True)

            left_hei, left_bal = dfs(node.left)
            if not left_bal:
                return 0, False
            right_hei, right_bal = dfs(node.right)
            return (
                1 + max(left_hei, right_hei),
                left_bal and right_bal and abs(left_hei - right_hei) <= 1,
            )

        return dfs(root)[1]
