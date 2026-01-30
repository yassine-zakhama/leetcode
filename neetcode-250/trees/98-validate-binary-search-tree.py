from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val, valid = [None], [True]

        def do_validate(node):
            if not node:
                return

            do_validate(node.left)
            if val[0] == None:
                val[0] = node.val
            elif val[0] < node.val:
                val[0] = node.val
            else:
                valid[0] = False
                return
            do_validate(node.right)

        do_validate(root)
        return valid[0]
