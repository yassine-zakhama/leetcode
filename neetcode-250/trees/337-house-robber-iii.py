from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)

            take_left, skip_left = dfs(node.left)
            take_right, skip_right = dfs(node.right)

            best_left = max(take_left, skip_left)
            best_right = max(take_right, skip_right)

            return (node.val + skip_left + skip_right, best_left + best_right)

        return max(dfs(root))
