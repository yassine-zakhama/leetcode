import { TreeNode } from "./treeNode";

function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
	if (!root) {
		return !subRoot;
	}
	return isSameTree(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
}

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
	if (!p || !q) {
		return !p && !q;
	} else {
		return p.val === q.val && isSameTree(q.left, p.left) && isSameTree(q.right, p.right);
	}
}
