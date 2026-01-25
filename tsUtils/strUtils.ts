export const StrUtils = {
	isDigit,
	isLowerCase,
	isUpperCase,
	isAlphabetic,
	isAlphanumeric
};

function isDigit(char: string): boolean {
	return char >= "0" && char <= "9";
}

function isLowerCase(char: string): boolean {
	return char >= "a" && char <= "z";
}

function isUpperCase(char: string): boolean {
	return char >= "A" && char <= "Z";
}

function isAlphabetic(char: string): boolean {
	return isUpperCase(char) || isLowerCase(char);
}

function isAlphanumeric(char: string): boolean {
	return isDigit(char) || isAlphabetic(char);
}
