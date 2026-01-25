function twoSum(nums: number[], target: number): number[] {
  const numIndices = new Map<number, number>();
  for (let i = 0; i < nums.length; ++i) {
    const n = nums[i];
    const searchedNumberIndex = numIndices.get(target - n);
    if (searchedNumberIndex !== undefined) {
      return [i, searchedNumberIndex];
    } else {
      numIndices.set(n, i);
    }
  }

  return [];
}
