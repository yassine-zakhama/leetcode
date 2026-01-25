function validPalindrome(s: string): boolean {
	let i = 0,
		j = s.length - 1;

	while (i < j) {
		const leftChar = s.charAt(i).toLocaleLowerCase();
		const rightChar = s.charAt(j).toLocaleLowerCase();
		if (leftChar !== rightChar) {
			return isPalindrome(s.slice(i, j)) || isPalindrome(s.slice(i + 1, j + 1));
		}
		++i;
		--j;
	}

	return true;
}

function isPalindrome(s: string): boolean {
	let i = 0,
		j = s.length - 1;

	while (i < j) {
		const leftChar = s.charAt(i).toLocaleLowerCase();
		const rightChar = s.charAt(j).toLocaleLowerCase();
		if (leftChar !== rightChar) {
			return false;
		}
		++i;
		--j;
	}

	return true;
}
