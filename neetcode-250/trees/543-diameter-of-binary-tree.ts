import { TreeNode } from "./treeNode";

function diameterOfBinaryTree(root: TreeNode | null): number {
	let res = 0;
	const [leftHeight, rightHeight] = dfs(root);
	return Math.max(res, leftHeight + rightHeight);

	function dfs(node: TreeNode | null): number[] {
		if (!node) {
			return [-1, -1];
		}

		const left = dfs(node.left);
		const leftHeight = Math.max(left[0], left[1]) + 1;
		const right = dfs(node.right);
		const rightHeight = Math.max(right[0], right[1]) + 1;
		res = Math.max(res, leftHeight + rightHeight);
		return [leftHeight, rightHeight];
	}
}
