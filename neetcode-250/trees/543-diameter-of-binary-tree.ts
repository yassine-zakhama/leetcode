import { TreeNode } from "./treeNode";

function diameterOfBinaryTree(root: TreeNode | null): number {
	let res = 0;
	dfs(root);
	return res;

	function dfs(node: TreeNode | null): number {
		if (!node) {
			return 0;
		}

		const leftHeight = dfs(node.left);
		const rightHeight = dfs(node.right);
		res = Math.max(res, leftHeight + rightHeight);
		return 1 + Math.max(leftHeight, rightHeight);
	}
}
