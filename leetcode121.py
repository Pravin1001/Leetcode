class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins=99999999
        maxs=0
        for i in range(len(prices)):
            mins=min(prices[i],mins)
            maxs=max(prices[i]-mins,maxs)
        return maxs
