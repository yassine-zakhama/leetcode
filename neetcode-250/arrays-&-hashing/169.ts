function majorityElement(nums: number[]): number {
	let numCount = new Map<number, number>();
	let res = 0,
		resCount = 0;
	for (let n of nums) {
		const newCount = (numCount.get(n) ?? 0) + 1;
		numCount.set(n, newCount);
		if (newCount > resCount) {
			res = n;
			resCount = newCount;
		}
	}
	return res;
}
