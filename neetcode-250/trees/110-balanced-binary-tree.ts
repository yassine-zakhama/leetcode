import { TreeNode } from "./treeNode";

interface NodeRes {
	balanced: boolean;
	height: number;
}

function isBalanced(root: TreeNode | null): boolean {
	return dfs(root).balanced;

	function dfs(node: TreeNode | null): NodeRes {
		if (!node) {
			return { balanced: true, height: 0 };
		}

		const left = dfs(node.left);
		const right = dfs(node.right);
		const balanced = left.balanced && right.balanced && Math.abs(left.height - right.height) <= 1;
		return { balanced, height: 1 + Math.max(left.height, right.height) };
	}

	function getHeight(res: (boolean | number)[]): number {
		return res[1] as number;
	}
}
