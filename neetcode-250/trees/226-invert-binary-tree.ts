import { TreeNode } from "./treeNode";

function invertTree(root: TreeNode | null): TreeNode | null {
	if (!root) {
		return null;
	}

	const left = root.left;
	root.left = invertTree(root.right);
	root.right = invertTree(left);
	return root;
}
