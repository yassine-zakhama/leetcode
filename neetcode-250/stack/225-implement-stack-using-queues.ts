class MyStack {
	private queue: number[];

	constructor() {
		this.queue = [];
	}

	push(x: number): void {
		this.queue.unshift(x);
	}

	pop(): number {
		let elementsUntilTop = this.queue.length - 1;
		while (elementsUntilTop) {
			this.queue.unshift(this.queue.shift()!);
			--elementsUntilTop;
		}
		return this.queue.shift()!;
	}

	top(): number {
		const top = this.pop();
		this.queue.unshift(top);
		return top;
	}

	empty(): boolean {
		return this.queue.length === 0;
	}
}
