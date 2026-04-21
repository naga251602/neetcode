class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        min_val = prices[0]

        for i in range(len(prices)):
            prof = max(prof, prices[i] - min_val)
            min_val = min(prices[i], min_val)

        return prof