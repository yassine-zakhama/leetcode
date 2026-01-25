function removeElement(nums: number[], val: number): number {
	let i = 0,
		j = nums.length - 1;

	while (i < j) {
		if (nums[i] !== val) {
			++i;
		} else {
			nums[i] = nums[j];
			--j;
		}
	}

	if (j >= 0 && nums[j] == val) {
		--j;
	}
	return j < 0 ? 0 : j + 1;
}
