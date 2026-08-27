class Solution(object):
    def maxProfit(self, prices):
        array=[]
        array.append(prices[0])
        minsum=array[0]
        max_profit=0
        for i in range(len(prices)):
            minsum=min(minsum,prices[i])
            max_profit = max(max_profit, prices[i] - minsum)
        return max_profit
        