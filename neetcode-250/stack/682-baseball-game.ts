function calPoints(operations: string[]): number {
	const nums: number[] = [];

	for (let op of operations) {
		const numsLen = nums.length;
		switch (op) {
			case "+":
				nums.push(nums[numsLen - 1] + nums[numsLen - 2]);
				break;

			case "D":
				nums.push(nums[numsLen - 1] * 2);
				break;

			case "C":
				nums.pop();
				break;

			default:
				nums.push(Number.parseInt(op));
		}
	}

	let res = 0;
	nums.forEach(n => (res += n));
	return res;
}
