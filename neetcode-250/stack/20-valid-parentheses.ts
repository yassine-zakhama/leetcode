function isValid(s: string): boolean {
	const closing: Record<string, string> = {
		"{": "}",
		"(": ")",
		"[": "]"
	};

	const expected: string[] = [];
	for (let c of s) {
		if (c in closing) {
			expected.push(closing[c]);
		} else if (expected.pop() !== c) {
			return false;
		}
	}

	return expected.length === 0;
}
