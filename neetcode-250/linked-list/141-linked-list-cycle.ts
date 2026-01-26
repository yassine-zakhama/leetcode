import { ListNode } from "./listNode";

function hasCycle(head: ListNode | null): boolean {
	let slow = head,
		fast = head?.next;

	while (fast) {
		if (slow == fast) {
			return true;
		}
		slow = slow?.next ?? null;
		fast = fast.next?.next;
	}

	return false;
}
