class Solution:

    def finalPrices(self, prices: List[int]) ->List[int]:
        result = prices.copy()
        stack = deque()
        i = 0
        while i < len(prices):
            while stack and prices[stack[-1]] >= prices[i]:
                result[stack.pop()] -= prices[i]
            stack.append(i)
            i += 1
        return result
