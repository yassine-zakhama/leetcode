class MyQueue {
	private stack1: number[];
	private stack2: number[];

	constructor() {
		this.stack1 = [];
		this.stack2 = [];
	}

	push(x: number): void {
		this.stack1.push(x);
	}

	pop(): number {
		if (!this.stack2.length) {
			while (this.stack1.length) {
				this.stack2.push(this.stack1.pop()!);
			}
		}
		return this.stack2.pop()!;
	}

	peek(): number {
		const top = this.pop();
		this.stack2.push(top);
		return top;
	}

	empty(): boolean {
		return this.stack1.length === 0 && this.stack2.length === 0;
	}
}
