from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if not root:
            return new_node

        parent = root
        while True:
            if parent.val < val:
                if parent.right:
                    parent = parent.right
                else:
                    break
            elif parent.left:
                parent = parent.left
            else:
                break

        if parent.val > val:
            parent.left = new_node
        else:
            parent.right = new_node

        return root

    def insertIntoBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST2(root.right, val)
        elif root.val > val:
            root.left = self.insertIntoBST2(root.left, val)
        return root
