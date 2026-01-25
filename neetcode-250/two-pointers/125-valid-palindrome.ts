import { StrUtils } from "../../tsUtils/strUtils";

function isPalindrome(s: string): boolean {
	let i = 0,
		j = s.length - 1;

	while (i < j) {
		const leftChar = s.charAt(i).toLocaleLowerCase();
		if (!StrUtils.isAlphanumeric(leftChar)) {
			++i;
			continue;
		}

		const rightChar = s.charAt(j).toLocaleLowerCase();
		if (!StrUtils.isAlphanumeric(rightChar)) {
			--j;
			continue;
		}

		if (leftChar !== rightChar) {
			return false;
		}
		++i;
		--j;
	}

	return true;
}
