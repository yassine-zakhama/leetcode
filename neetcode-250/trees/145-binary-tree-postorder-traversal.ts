import { TreeNode } from "./treeNode";

function postorderTraversal(root: TreeNode | null): number[] {
	const res: number[] = [];
	doTraverse(root);
	return res;

	function doTraverse(node: TreeNode | null) {
		if (node) {
			doTraverse(node.left);
			doTraverse(node.right);
			res.push(node.val);
		}
	}
}
