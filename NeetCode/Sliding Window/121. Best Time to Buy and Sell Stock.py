from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i] 
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        
        return max_profit

# Example usage:
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))  # Output: 5
print(solution.maxProfit([7,6,4,3,1]))    # Output: 0