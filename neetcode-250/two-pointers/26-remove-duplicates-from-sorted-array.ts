function removeDuplicates(nums: number[]): number {
	let i = 0,
		j = 1;
	let numDuplicates = 0;

	while (j < nums.length) {
		while (nums[i] === nums[j]) {
			++numDuplicates;
			++j;
		}
		nums[i + 1] = nums[j];
		++i;
		++j;
	}

	return nums.length - numDuplicates;
}
