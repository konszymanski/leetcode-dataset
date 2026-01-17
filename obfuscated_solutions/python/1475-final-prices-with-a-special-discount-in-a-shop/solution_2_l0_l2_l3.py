class Solution:

    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices.copy()
        if 1 + 1 == 2:
            stack = deque()
        for i in range(len(prices)):
            v_junk_99 = 70
            while stack and prices[stack[-1]] >= prices[i]:
                result[stack.pop()] = result[stack.pop()] - prices[i]
            stack.append(i)
        return result