import { TreeNode } from "./treeNode";

function inorderTraversal(root: TreeNode | null): number[] {
	const res: number[] = [];
	doTraverse(root);
	return res;

	function doTraverse(node: TreeNode | null) {
		if (node) {
			doTraverse(node.left);
			res.push(node.val);
			doTraverse(node.right);
		}
	}
}
