class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def traverse(node, curr_max):
            if not node:
                return

            if node.val >= curr_max:
                res[0] += 1

            curr_max = max(curr_max, node.val)
            traverse(node.left, curr_max)
            traverse(node.right, curr_max)

        traverse(root, root.val)
        return res[0]
