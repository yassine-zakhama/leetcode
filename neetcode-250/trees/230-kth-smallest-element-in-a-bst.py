from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, remaining = [root.val], [k]

        def do_find(node):
            if not node:
                return

            do_find(node.left)

            remaining[0] -= 1
            if not remaining[0]:
                res[0] = node.val
                return

            do_find(node.right)

        do_find(root)
        return res[0]
