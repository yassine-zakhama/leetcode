function merge(nums1: number[], m: number, nums2: number[], n: number): void {
	let i1 = m - 1,
		i2 = n - 1;
	let j = nums1.length - 1;

	while (i1 >= 0 && i2 >= 0) {
		if (nums1[i1] >= nums2[i2]) {
			nums1[j] = nums1[i1];
			--i1;
		} else {
			nums1[j] = nums2[i2];
			--i2;
		}
		--j;
	}

	while (i2 >= 0) {
		nums1[j] = nums2[i2];
		--i2;
		--j;
	}
}
