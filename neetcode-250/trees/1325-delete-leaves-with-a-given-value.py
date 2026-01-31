from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def do_remove(node):
            if not node:
                return False
            elif not node.left and not node.right:
                return node.val == target

            if do_remove(node.left):
                node.left = None
            if do_remove(node.right):
                node.right = None
            return not node.left and not node.right and node.val == target

        return None if do_remove(root) else root
