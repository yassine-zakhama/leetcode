import { TreeNode } from "./treeNode";

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
	if (!p || !q) {
		return !p && !q;
	} else {
		return p.val === q.val && isSameTree(q.left, p.left) && isSameTree(q.right, p.right);
	}
}
