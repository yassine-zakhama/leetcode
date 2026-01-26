import { TreeNode } from "./treeNode";

function preorderTraversal(root: TreeNode | null): number[] {
	const res: number[] = [];
	doTraverse(root);
	return res;

	function doTraverse(node: TreeNode | null) {
		if (node) {
			res.push(node.val);
			doTraverse(node.left);
			doTraverse(node.right);
		}
	}
}
