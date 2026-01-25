function containsNearbyDuplicate(nums: number[], k: number): boolean {
	const seen = new Set([nums[0]]);
	let i = 0;
	for (let j = 1; j < nums.length; ++j) {
		if (j - i > k) {
			seen.delete(nums[i]);
			++i;
		}

		if (seen.has(nums[j])) {
			return true;
		}

		seen.add(nums[j]);
	}

	return false;
}
