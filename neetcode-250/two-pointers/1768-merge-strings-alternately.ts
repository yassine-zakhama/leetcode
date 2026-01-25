function mergeAlternately(word1: string, word2: string): string {
	let i1 = 0,
		i2 = 0;
	let res: string[] = [];

	while (i1 < word1.length && i2 < word2.length) {
		res.push(word1[i1], word2[i2]);
		++i1;
		++i2;
	}

	if (i1 < word1.length) {
		res.push(word1.slice(i1));
	} else if (i2 < word2.length) {
		res.push(word2.slice(i2));
	}

	return res.join("");
}
