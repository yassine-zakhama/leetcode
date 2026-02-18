from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (-1, -1)

            left_hei, left_diam = dfs(node.left)
            right_hei, right_diam = dfs(node.right)
            return (
                max(left_hei, right_hei) + 1,
                max(left_diam, right_diam, left_hei + right_hei + 2),
            )

        return max(dfs(root))
