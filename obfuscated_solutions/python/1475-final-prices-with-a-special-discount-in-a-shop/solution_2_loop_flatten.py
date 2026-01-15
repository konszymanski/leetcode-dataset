class Solution:

    def finalPrices(self, prices: List[int]) ->List[int]:
        result = prices.copy()
        stack = deque()
        for i in range(len(prices)):
            while True:
                if not (stack and prices[stack[-1]] >= prices[i]):
                    break
                result[stack.pop()] -= prices[i]
            stack.append(i)
        return result
