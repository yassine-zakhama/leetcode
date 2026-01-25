function longestCommonPrefix(strs: string[]): string {
	let shortest = 200;
	strs.forEach(s => (shortest = Math.max(shortest, s.length)));

	const res: string[] = [];
	for (let i = 0; i < shortest; ++i) {
		const char = strs[0].charAt(i);
		for (let j = 1; j < strs.length; ++j) {
			if (strs[j].charAt(i) !== char) {
				return res.join("");
			}
		}
		res.push(char);
	}

	return res.join("");
}
