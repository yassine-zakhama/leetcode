class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# O(h)
class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        SMALLER, GREATER = min(p.val, q.val), max(p.val, q.val)

        def dfs(node):
            if SMALLER <= node.val <= GREATER:
                return node
            return dfs(node.left) if node.val > GREATER else dfs(node.right)

        return dfs(root)
