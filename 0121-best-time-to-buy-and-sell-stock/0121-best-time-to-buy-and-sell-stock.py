class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Initialize max_profit
        max_profit = 0

        # Set the left and right pointers
        length = len(prices)
        left = 0
        right = left + 1

        # Iterate over the window
        while (right < length):

            if prices[left] < prices[right]:
                cur_profit = prices[right] - prices[left]
                if cur_profit > max_profit:
                    max_profit = cur_profit
                right = right + 1
            
            else:
                left = right
                right = right + 1
            
        return max_profit
        