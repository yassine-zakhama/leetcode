/**
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

var guess = function (num: number): number {
	return 0;
};

function guessNumber(n: number): number {
	let lower = 1,
		upper = n;

	while (true) {
		const mid = Math.trunc((lower + upper) / 2);
		const g = guess(mid);
		if (g === -1) {
			upper = mid - 1;
		} else if (g === 1) {
			lower = mid + 1;
		} else {
			return mid;
		}
	}
}
