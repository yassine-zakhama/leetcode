import { ListNode } from "./listNode";

function reverseList(head: ListNode | null): ListNode | null {
	if (!head) {
		return null;
	}

	let next = head.next;
	head.next = null;

	while (next) {
		let temp = next.next;
		next.next = head;
		head = next;
		next = temp;
	}

	return head;
}

function reverseListRecursively(head: ListNode | null): ListNode | null {
	if (head?.next) {
		const temp = head;
		doReverse(head);
		temp.next = null;
	}
	return head;

	function doReverse(node: ListNode): ListNode {
		if (!node.next) {
			head = node;
			return node;
		}

		const next = doReverse(node.next);
		next.next = node;
		return node;
	}
}
