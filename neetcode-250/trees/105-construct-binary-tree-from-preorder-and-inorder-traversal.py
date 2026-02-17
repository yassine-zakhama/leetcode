from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        in_indices = {val: i for i, val in enumerate(inorder)}

        def build(root_pre_idx, start_in, end_in):
            root_val = preorder[root_pre_idx]
            root_in_idx = in_indices[root_val]
            left_size, right_size = root_in_idx - start_in, end_in - root_in_idx

            root = TreeNode(root_val)
            if left_size > 0:
                root.left = build(root_pre_idx + 1, start_in, root_in_idx - 1)
            if right_size > 0:
                root.right = build(
                    root_pre_idx + left_size + 1, root_in_idx + 1, end_in
                )
            return root

        return build(0, 0, len(inorder) - 1)
