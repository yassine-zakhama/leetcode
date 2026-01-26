function maxProfit(prices: number[]): number {
	let maxProfit = 0,
		left = 0;

	for (let right = 1; right < prices.length; ++right) {
		const buyPrice = prices[left],
			sellPrice = prices[right];

		if (buyPrice > sellPrice) {
			left = right;
		} else {
			maxProfit = Math.max(maxProfit, sellPrice - buyPrice);
		}
	}

	return maxProfit;
}
